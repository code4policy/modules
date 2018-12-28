# Sample APIs

## Setup
1. Make sure to install the python `requests` library, by entering `pip install requests` into the terminal
2. To make JSON output more readable in Sublime Text, follow the instructions [here](https://blog.adriaan.io/sublime-pretty-json.html)

## FEC API
1. Take a look around at the [FEC API documentation](https://api.open.fec.gov/developers/)
2. Before running the FEC API script, you will need your own API key, which you can find [here](https://api.data.gov/signup/)
3. Since you don't want to make your key public, add your key to your environment variables by typing `export FECKEY='<your_key_here>'` into the terminal
4. Run the following command in your terminal to see candidates who ran for office in Massachusetts in 2016:
```
python fecAPI.py
```
5. The script will also save the raw json results in a file called `fec_api_results.json`. To make these results more readable, follow the instructions in the **Setup** section above

## Huffington Post Polls API
1. Take a look around at the [Huffington Post Polls documentation](https://app.swaggerhub.com/apis/huffpostdata/pollster-api/2.0.0#/)
2. Run the following command in your terminal to see links to the acutal polls:
```
python huffpostAPI.py
```
3. The script will also save the raw json results in a file called `huffpost_api_results.json`. To make these results more readable, follow the instructions in the **Setup** section above

