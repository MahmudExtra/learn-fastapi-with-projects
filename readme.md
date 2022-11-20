### Some Notes

_To run a cloned repo from github , first we have to install all the packages for the fast api_

**To do that do the following commands**

```
pip install -r requirements.txt
```

**To run the server**

```
uvicorn main:app --reload
```

**To run the server in background**

```
nohup uvicorn main:app --reload &
```

**To stop the server**

```
kill -9 $(lsof -t -i:8000)
```

**To check the logs**

```
tail -f nohup.out
```

**To check the server status**

```
lsof -i:8000
```
