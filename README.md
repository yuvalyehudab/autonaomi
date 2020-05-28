[![Build Status](https://travis-ci.com/yuvalyehudab/autonaomi.svg?branch=master)](https://travis-ci.com/yuvalyehudab/autonaomi)


# autonaomi
A project for advanced system design class

## Installation

1. Clone the repository and enter it:

    ```sh
    $ git clone git@github.com:yuvalyehudab/autonaomi.git
    ...
    $ cd autonaomi/
    ```

2. Run the installation script and activate the virtual environment:

    ```sh
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    [autonaomi] $ # we're good to go!
    ```

3. To check that everything is working as expected, run the tests:


    ```sh
    $ pytest tests/
    ...
    ```

4. Try:

    ```sh
    bash .scripts/run-pipelines
    python -m autonaomi.client upload-sample -h 'localhost' -p 7700 ../Downloads/sample.mind.gz
    ```

    open chrome in 'localhost:9030', you should see all the users in the database now.

## Parser addition

0. requirements:
    - the parser is a function that gets data and path, like that:

    ```sh
    my_parsing_func(snapshot, path)
    ```
    - it returns jsonable object

1. import the function

    ```sh
    from my_parser_file import my_parsing_func
    ```
2. add it to the dictionary where the other parsers are - autonaomi/parsers/run_parser.py:

    ```sh
    parsers_dict = {
    'feelings': feelings,
    'pose': pose,
    'depth_image': depth_image,
    'parser_name': my_parsing_func,
    'color_image': color_image
    }
    ```