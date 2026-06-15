CREATE TABLE IF NOT EXISTS quizzes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    correct_option INTEGER NOT NULL,
    explanation TEXT
);

CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER,
    answer TEXT NOT NULL
);

INSERT INTO quizzes (title)
VALUES ('Matematicas Basicas');

INSERT INTO questions
(
    quiz_id,
    question,
    option1,
    option2,
    option3,
    option4,
    correct_option,
    explanation
)
VALUES
(
    1,
    'Cuanto es 5 + 3?',
    '6',
    '7',
    '8',
    '9',
    '3',
    "5+3=8"
),

(
    1,
    'Cuanto es 10 - 4?',
    '5',
    '6',
    '7',
    '8',
    '2',
    "10-4=6"
),

(
    1,
    'Cuanto es 3 x 4?',
    '7',
    '10',
    '12',
    '14',
    '3',
    "3x4=12"
),

(
    1,
    'Cuanto es 20 / 5?',
    '2',
    '3',
    '4',
    '5',
    '3',
    "20/5=4"
),

(
    1,
    'Cual es el resultado de 2^2?',
    '2',
    '4',
    '6',
    '8',
    '2',
    "2^2=2x2=4"
);

INSERT INTO quizzes (title)
VALUES ('Matematicas Basicas 2');

INSERT INTO questions
(
    quiz_id,
    question,
    option1,
    option2,
    option3,
    option4,
    correct_option,
    explanation
)
VALUES
(
    2,
    'Cuanto es 7 + 4 - 3?',
    '6',
    '7',
    '8',
    '9',
    '3',
    "7+4-3=8"
),

(
    2,
    'Cuanto es 4 - 2 / 2?',
    '1',
    '4',
    '2',
    '3',
    '4',
    "4-2/2=4-1=3"
),

(
    2,
    'Cuanto es 5 + 2 x 3?',
    '11',
    '21',
    '17',
    '10',
    '1',
    "5+2x3=11"
),

(
    2,
    'Cuanto es 4^3 + 5?',
    '59',
    '16.384',
    '69',
    '17',
    '3',
    "4^3+5=4x4x4+5=64+5=69"
),

(
    2,
    'Cual es el resultado de 7 x (5-3) ?',
    '32',
    '14',
    '25',
    '8',
    '2',
    "7x(5-3)=7x2=14"
);

INSERT INTO quizzes (title)
VALUES ('Matematicas Basicas 3');