import sqlite3

con = sqlite3.connect("YSP.sqlite")

# Пипец

con.executescript('''
CREATE TABLE IF NOT EXISTS category (
 category_id INTEGER PRIMARY KEY AUTOINCREMENT,
 category_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS users (
 users_id INTEGER PRIMARY KEY AUTOINCREMENT,
 users_login VARCHAR(30),
 users_password VARCHAR(30),
 OG REAL,
 OT REAL,
 OB REAl,
 VB REAL,
 CG REAL,
 VG REAL,
 SHG1 REAL,
 SHG2 REAL,
 H REAL,
 SHS REAL,
 OSH REAL,
 DPL REAL,
 OP REAL,
 OZ REAL,
 DR REAL
);

CREATE TABLE IF NOT EXISTS measure (
 measure_id INTEGER PRIMARY KEY AUTOINCREMENT,
 measure_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS math_formula (
 math_formula_id INTEGER PRIMARY KEY AUTOINCREMENT,
 formula VARCHAR(300),
 description VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS detail (
 detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
 detail_name VARCHAR(50),
 math_formula_id INTEGER,
 FOREIGN KEY (math_formula_id) REFERENCES math_formula (math_formula_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS detail_measure (
 detail_measure_id INTEGER PRIMARY KEY AUTOINCREMENT,
 detail_id INTEGER,
 measure_id INTEGER,
 FOREIGN KEY (detail_id) REFERENCES detail (detail_id) ON DELETE CASCADE,
 FOREIGN KEY (measure_id ) REFERENCES measure (measure_id ) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pattern (
 pattern_id INTEGER PRIMARY KEY AUTOINCREMENT,
 pattern_name VARCHAR(70),
 category_id INTEGER,
 FOREIGN KEY (category_id) REFERENCES category (category_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pattern_detail (
 pattern_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
 pattern_id INTEGER,
 detail_id INTEGER,
 FOREIGN KEY (pattern_id) REFERENCES pattern (pattern_id) ON DELETE CASCADE,
 FOREIGN KEY (detail_id) REFERENCES detail (detail_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS favorite (
 favorite_id INTEGER PRIMARY KEY AUTOINCREMENT,
 user_id INTEGER,
 pattern_id INTEGER,
 FOREIGN KEY (users_id) REFERENCES users (users_id) ON DELETE CASCADE,
 FOREIGN KEY (pattern_id) REFERENCES pattern (pattern_id) ON DELETE CASCADE
);
''')

con.executescript('''
INSERT INTO category (category_name)
VALUES
('Блуза'),
('Болеро'),
('Водолазка'),
('Джемпер'),
('Жилет'),
('Лонгслив'),
('Майка'),
('Платье'),
('Поло'),
('Пуловер'),
('Рубашка'),
('Сарафан'),
('Туника'),
('Футболка'),
('Худи'),
('Брюки'),
('Шорты'),
('Юбка');



INSERT INTO users (users_login, users_password, OG, OT, OB, VB, CG, VG, SHG1, SHG2, H, SHS, OSH, DPL, OP, OZ, DR)
VALUES
('NiShiGara','123456789qwerty',104, 84, 110, 21, 22, 31, 44, 34, 11, 38, 40, 12, 32, 17, 62),
('srf_adlr','qwertasdfzxc',80, 60, 86, 18, 19, 25, 32, 28, 8, 32,  34, 11, 26, 14, 60),
('burakov.a.a','12348765bur',112, 96, 122, 22, 23, 33, 48, 36, 12, 40, 42, 13, 34, 18, 63),
('Aitan','qwertzxcFdW35',108, 90, 116, 22, 22.5, 32, 46, 35, 11.5, 39, 41, 13, 33, 17.5, 63),
('Nathaniel','Po3jv83fvF',88, 68, 94, 18, 20, 27, 36, 30, 9, 34, 36, 11, 28, 15, 61),
('IvanovIvan','Jdhe3421NBq',84, 64, 90, 19, 19.5, 26, 34, 29, 8.5, 33, 35, 11, 27, 14.5, 60),
('cur_tess','123zxcvbasQWE',100, 80, 106, 21, 21.5, 30, 42, 33, 10.5, 37, 39, 12, 31, 16.5, 62),
('yulexer','16q04w2001rty',96, 76, 102, 20, 21, 29, 40, 32, 10, 36, 38, 12, 30, 16, 62);


INSERT INTO pattern (pattern_name, category_id)
VALUES
('Футболка поло', 14),
('Футболка Дженни', 14),
('Футболка Магда', 14),
('Блуза-американка', 1),
('Блуза без рукава', 1),
('Блуза с рукавом', 1),
('Рубашка Поло', 11),
('Классическая рубашка', 11),
('Пляжная рубашка', 11),
('Пижамная рубашка', 11),
('Юбка-карандаш', 18),
('Юбка-солнце', 18),
('Юбка годе', 18),
('Юбка трапеция', 18),
('Классические брюки', 16),
('Брюки бананы', 16),
('Брюки скинни', 16),
('Брюки карго', 16),
('Бермуды', 17),
('Классические шорты', 17),
('Капри', 17),
('Бриджи', 17),
('Платье-футляр', 8),
('Платье-трапеция', 8),
('Платье-рубашка', 8),
('Платье-баллон', 8);


INSERT INTO favorite (users_id, pattern_id)
VALUES
(1,5),
(1,15),
(1,3),
(1,21),
(1,6),
(1,2),
(2,16),
(2,13),
(2,22),
(2,23),
(2,24),
(2,10),
(3,19),
(3,20),
(3,1),
(3,7),
(3,4),
(3,9),
(3,14),
(4,5),
(4,1),
(4,2),
(4,6),
(4,18),
(4,24),
(4,25),
(4,20),
(5,17),
(5,13),
(5,12),
(5,11),
(5,2),
(6,4),
(6,8),
(6,12),
(7,23),
(7,21),
(7,15),
(7,14),
(7,23),
(7,1),
(7,4);

INSERT INTO measure (measure_name)
VALUES
();

INSERT INTO math_formula (formula, description)
VALUES
();

''')

# сохраняем информацию в базе данных
con.commit()
cursor = con.cursor()

# cursor.execute("SELECT * FROM pattern")
# print(cursor.fetchall())

con.close()

#проверка
