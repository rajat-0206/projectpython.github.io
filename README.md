## HOW TO RUN

1. Install the required package using following command :
    ```
    pip install -r requirements.txt
    ```

2. There is a small issue with firebase package. To fix it first find the path where it is installed.
    ```
    pip show python-firebase
    ```

3. Now go to the Location of the package. Change the filename async.py to asyncn.py

4. Change the import statement in __init__py and firebase.py
    ``` 
    original : from .async import process_pool
    after changing: from .asyncn import process_pool

5. Now come to root of the project and run the project by following command.
    ```
    python "Jumble Juggle.py"
    ```