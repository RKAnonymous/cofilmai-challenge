
1. Create swagger doc with the command below:

```curl -0 localhost:8000/openapi.json >> openapi.json```

2. Pull and write trending data into DB using ensembledata's TikTok API:
    Endpoint: ```https://www.ensembledata.com/apis/tt/hashtag/posts```

3. Run trending data extracter script every hour:
    I would suggest to use more advanced tools like airflow to develop such kind of ETL pipelines.

    I tried setting up ```crontab```:

    1. Open cronjobs list.
        ```crontab -e```
    2. Add this command to the end.
        ```0 * * * * /path/to/project/cofilmai-challenge/venv/bin/python /path/to/project/cofilmai-challenge/services/trends/src/utils/save_trending_data.py```
    3. Save and close. ```CTRL+S```, ```CTRL+X```
    4. Check. ```crontab -l``` command should print out existing jobs list and your job should appear in the end.

    ```BUT: It seems cron job has some issues executing with asynchronous task```

    Then I found a way around with wrapping ```trends``` function with custom asynchronous ```scheduler```.
    As [here](/services/trends/src/utils/save_trending_data.py#L30)