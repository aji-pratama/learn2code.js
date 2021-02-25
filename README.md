# Documentation

## Technologies

- Backend: `Django`
- Frontend: `VueJS` (Instance)
- Database: `SQLite` (DB file included for testing purpose)
- Styling/CSS: [Argon Design System](https://www.creative-tim.com/product/argon-design-system) by CreativeTim
- Javascript Intrepreter: [Js2Py](https://github.com/PiotrDabkowski/Js2Py) by Piotr Dabkowski

## Installation

1. `pip install -r requirements.txt`
2. `./manage.py runserver`

Access [`127.0.0.1:8000`](http://127.0.0.1:8000) or [`localhost:8000`](http://localhost:8000) (default Django development server) via browser

## Admin

Account for testing:

**url admin**: [`127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/)

**username**: `pdso`

**password**: `practicaldso`

The Admin User can do:

- Add new Lesson
- Create expected codes
- Add additional static assets (HTML, CSS, Javascript) ***for Web Output**
- Sort the lessons

## Apps

- The Apps have 2 output type
    - **console output**
    - **web output**
- The `answer_code` need to click button `Run` to validate the `answer_code`
- If the code is running and correct, the Next button will be enabled and the user can take the next lesson.
- The answer code will be store/save in the `session`, as long as the user has clicked the button `Run` So if the User leaves or closed the tab (browser), the ran `code` will not be lost.


## Data Model

[Lesson](https://www.notion.so/c8f5ba4335d149c99fb3359e53ed0e79)

[ExtraStatic (for Web Output)](https://www.notion.so/631d82ea10f948958be73586de29b28f)

[ExpectedAnswer](https://www.notion.so/fc3e4e3343b94352af0087a217a610e7)

## Validation System

Code will validate and will send 3 message in popup notification:

1. Code error
2. Code run successful but incorrect based in expected answer
3. Code run successful and correct based in expected answer, and the Next Button will be enabled.

### Console Output

In the console, the `answer_code` will execute using [Js2Py](https://github.com/PiotrDabkowski/Js2Py) and the `result` will validate, **is the result is in the** `expected_answers` that Admin defines in Admin Page? If correct it will show notification no. 3

### Web Output

In the web output, the method uses to validate it based on `answer_code` without compiling. So, if **the code is in the** `expected_answers` it will correct.
