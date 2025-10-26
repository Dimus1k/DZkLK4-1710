import sys
import os
from PySide6.QtWidgets import (QApplication, QWidget, QLabel,
                               QVBoxLayout, QHBoxLayout, QPushButton, QFrame)
from PySide6.QtGui import QFont, QPixmap, QPainter, QLinearGradient, QColor
from PySide6.QtCore import Qt


class GradientBackground(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor('#667eea'))
        gradient.setColorAt(1, QColor('#764ba2'))
        painter.fillRect(self.rect(), gradient)


class UserProfile(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройка графического интерфейса"""
        self.setGeometry(100, 100, 400, 650)
        self.setWindowTitle("Профиль пользователя - PySide6")
        self.setStyleSheet("background-color: #f8f9fa;")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Создание и расположение виджетов"""
        # Основной layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Верхняя часть с градиентным фоном
        self.createHeaderSection(main_layout)

        # Основная информация
        self.createProfileSection(main_layout)

        self.setLayout(main_layout)

    def createHeaderSection(self, layout):
        """Создание шапки с градиентным фоном"""
        header_frame = QFrame()
        header_frame.setFixedHeight(200)
        header_frame.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #667eea, stop:1 #764ba2);
                border: none;
            }
        """)

        header_layout = QVBoxLayout(header_frame)

        # Аватарка профиля
        avatar_frame = QFrame()
        avatar_frame.setFixedSize(120, 120)
        avatar_frame.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-radius: 60px;
                border: 4px solid white;
            }
        """)

        # Загрузка изображения профиля
        avatar_label = QLabel(avatar_frame)
        if os.path.exists("images/profile.png"):
            pixmap = QPixmap("images/profile.png")
            # Масштабируем изображение под круглую аватарку
            pixmap = pixmap.scaled(112, 112, Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                                   Qt.TransformationMode.SmoothTransformation)
            avatar_label.setPixmap(pixmap)
        else:
            # Fallback на инициалы если изображения нет
            avatar_label.setText("ДК")
            avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            avatar_label.setStyleSheet("""
                QLabel {
                    color: #667eea;
                    font-size: 24px;
                    font-weight: bold;
                    background: transparent;
                }
            """)
        avatar_label.setGeometry(0, 0, 120, 120)

        # Layout для центрирования аватарки
        avatar_container = QHBoxLayout()
        avatar_container.addStretch()
        avatar_container.addWidget(avatar_frame)
        avatar_container.addStretch()

        header_layout.addStretch()
        header_layout.addLayout(avatar_container)
        header_layout.addStretch()

        layout.addWidget(header_frame)

    def createProfileSection(self, layout):
        """Создание основной секции с информацией"""
        content_frame = QFrame()
        content_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: none;
            }
        """)

        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(30, 20, 30, 20)
        content_layout.setSpacing(15)

        # Имя и должность
        name_label = QLabel("Дмитрий Курников")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
            }
        """)

        position_label = QLabel("Студент 2ого курса")
        position_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        position_label.setStyleSheet("""
            QLabel {
                color: #7f8c8d;
                font-size: 16px;
                margin-bottom: 20px;
            }
        """)

        # Разделитель
        separator1 = QFrame()
        separator1.setFrameShape(QFrame.Shape.HLine)
        separator1.setStyleSheet("background-color: #ecf0f1;")

        # Биография
        bio_section = self.createInfoSection("Биография",
                                             "Уроженец города Вязники. Окончил школу №4 с серебряной медалью.Сейчас учусь в МАИ на направлении 'Инноватика' ")

        # Разделитель
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.Shape.HLine)
        separator2.setStyleSheet("background-color: #ecf0f1;")

        # Навыки
        skills_section = self.createInfoSection("Навыки",
                                                "Python, MySQL")

        # Разделитель
        separator3 = QFrame()
        separator3.setFrameShape(QFrame.Shape.HLine)
        separator3.setStyleSheet("background-color: #ecf0f1;")

        # Опыт работы
        exp_section = self.createExperienceSection()

        # Добавляем все виджеты (без кнопки)
        content_layout.addWidget(name_label)
        content_layout.addWidget(position_label)
        content_layout.addWidget(separator1)
        content_layout.addLayout(bio_section)
        content_layout.addWidget(separator2)
        content_layout.addLayout(skills_section)
        content_layout.addWidget(separator3)
        content_layout.addLayout(exp_section)
        content_layout.addStretch()

        layout.addWidget(content_frame)

    def createInfoSection(self, title, content):
        """Создание секции с заголовком и содержимым"""
        layout = QVBoxLayout()
        layout.setSpacing(8)

        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                font-size: 16px;
                font-weight: bold;
            }
        """)

        content_label = QLabel(content)
        content_label.setWordWrap(True)
        content_label.setStyleSheet("""
            QLabel {
                color: #34495e;
                font-size: 14px;
                line-height: 1.4;
            }
        """)

        layout.addWidget(title_label)
        layout.addWidget(content_label)

        return layout

    def createExperienceSection(self):
        """Создание секции опыта работы"""
        layout = QVBoxLayout()
        layout.setSpacing(8)

        title_label = QLabel("Опыт работы")
        title_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        layout.addWidget(title_label)

        # Опыт 1
        exp1_layout = QVBoxLayout()
        exp1_layout.setSpacing(2)

        exp1_title = QLabel("Сборщик электрических машин и аппаратов 2ого разряда")
        exp1_title.setStyleSheet("color: #2c3e50; font-size: 14px; font-weight: bold;")

        exp1_company = QLabel("ПАО 'ОСВАР'")
        exp1_company.setStyleSheet("color: #3498db; font-size: 13px;")

        exp1_period = QLabel("Лето 2023")
        exp1_period.setStyleSheet("color: #7f8c8d; font-size: 12px;")

        exp1_layout.addWidget(exp1_title)
        exp1_layout.addWidget(exp1_company)
        exp1_layout.addWidget(exp1_period)

        # Опыт 2
        exp2_layout = QVBoxLayout()
        exp2_layout.setSpacing(2)

        exp2_title = QLabel("Администратор")
        exp2_title.setStyleSheet("color: #2c3e50; font-size: 14px; font-weight: bold; margin-top: 10px;")

        exp2_company = QLabel("Панорама 360")
        exp2_company.setStyleSheet("color: #3498db; font-size: 13px;")

        exp2_period = QLabel("Июнь 2025-(по сей день)")
        exp2_period.setStyleSheet("color: #7f8c8d; font-size: 12px;")

        exp2_layout.addWidget(exp2_title)
        exp2_layout.addWidget(exp2_company)
        exp2_layout.addWidget(exp2_period)

        layout.addLayout(exp1_layout)
        layout.addLayout(exp2_layout)

        return layout


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserProfile()
    sys.exit(app.exec())
