-- insert sample projects
insert into
    `project` (
        `description`,
        `duration`,
        `id`,
        `name`,
        `parent`,
        `start_date`,
        `weight`
    )
values
    (
        'Python Scripts\nAllowed editors: vi, vim, emacs\nAll your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)\nAll your files should end with a new line\nThe first line of all your files should be exactly #!/usr/bin/python3\nYour code should use the pycodestyle (version 2.8.*)\nAll your files must be executable',
        NULL,
        '101',
        '0x00-python-hello_world',
        'alx-higher_level_programming',
        NULL,
        1
    );

insert into
    `project` (
        `description`,
        `duration`,
        `id`,
        `name`,
        `parent`,
        `start_date`,
        `weight`
    )
values
    (
        'Python Scripts\nAllowed editors: vi, vim, emacs\nAll your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)\nAll your files should end with a new line\nThe first line of all your files should be exactly #!/usr/bin/python3\nYour code should use the pycodestyle (version 2.8.*)\nAll your files must be executable',
        NULL,
        '102',
        '0x01-python-if_else_loops_functions',
        'alx-higher_level_programming',
        NULL,
        1
    );

insert into
    `project` (
        `description`,
        `duration`,
        `id`,
        `name`,
        `parent`,
        `start_date`,
        `weight`
    )
values
    (
        'Python Scripts\nAllowed editors: vi, vim, emacs\nAll your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)\nAll your files should end with a new line\nThe first line of all your files should be exactly #!/usr/bin/python3\nYour code should use the pycodestyle (version 2.8.*)\nAll your files must be executable',
        NULL,
        '103',
        '0x03-python-data_structures',
        'alx-higher_level_programming',
        NULL,
        1
    );

-- insert sample tasks
insert into
    `task` (
        `avg_denom`,
        `description`,
        `id`,
        `name`,
        `output`,
        `pid`,
        `weight`
    )
values
    (
        5,
        'Write a Python script that prints exactly \"Programming is like building a multilingual puzzle, followed by a new line.',
        '101',
        '2-print',
        '\"Programming is like building a multilingual puzzle\n',
        '101',
        1
    );

insert into
    `task` (
        `avg_denom`,
        `description`,
        `id`,
        `name`,
        `output`,
        `pid`,
        `weight`
    )
values
    (
        5,
        'Write a Python script in which the output should be: the number, followed by Battery street, followed by a new line',
        '102',
        '3-print_number',
        '98 Battery street\n',
        '101',
        1
    );
