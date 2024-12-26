"""
### Question:
Design a session-based authentication system where each user session generates a new token with a specified time-to-live (TTL) expiration. The TTL expiration is calculated as the current time plus the time-to-live
in seconds.  If a token is renewed, the TTL is extended to the time-to-live seconds after the time of the renewal. 

There are three types of queries in this system:

1. `"generate <token_id><current_time>"`: Creates a new token with the given `token_id` and `current_time`.
2. `"renew <token_id> <current_time>"`: Renews an unexpired token with the given `token_id` and current_time . If there is no unexpired token with the specified token_id, the request is ignored
3. `"count current_time"`: Returns the number of unexpired tokens at the specified `current_time`.

Tokens expires at a specific time and any action is performed at the same time, the token's expiration occurs before any other actions are carried out.

Example:
- Input: 
   ```
   time_to_live = 5
   queries = ["generate aaa 1", "renew aaa 2", "count 6", "generate bbb 7", "renew aaa 8", "renew bbb 10", "count 15"]
   ```

| Query No. | Action    | Generated Token | Timestamp | Expiry Timestamp | Unexpired Tokens |
|-----------|-----------|-----------------|-----------|------------------|------------------|
| 1         | Generate  | aaa             | 1         | 6                |                  |
| 2         | Renew     | aaa             | 2         | 7                |                  |
| 3         | Count     |                 | 6         |                  | 1                |
| 4         | Generate  | bbb             | 7         | 12               |                  |
| 5         | Renew     | aaa             | 8         | 13               |                  |
| 6         | Renew     | bbb             | 10        | 15               |                  |
| 7         | Count     |                 | 15        | -                | 0                |

- Output: 
   ```
   [1, 0]
   ```

Explanation:
- At t = 6, the only unexpired token is "aaa"
- At t = 15, all tokens have expired, so the count of unexpired token is 0


### Function Description:
Implement the function `getUnexpiredTokens` which:
- Takes in `time_to_live`(int), an integer indicating the time-to-live for a token.
- Takes in `queries`, a list of query strings in the format above.

### Returns:
int[]: the results from type 3 query in the same order it is given


Constraints:
- 1<=q<= 100000
- 1 < |queries| <= 10^5
- 1 <= time_to_live <= 10^8
- 1 <= current_time <= 10^8
- 1 <= [token_id] <= 5
- token_id consists only of lowercase letters and numbers
- All queries of type generate will contain unique values of token_id
- current_time is non-decreasing order in the queries

Test example :

Input :
time_to_live = 35
queries[] size q = 6
queries = ["generate token1 3", "count 4", "generate token2 6", "count 7", "generate token3 11", "count 41"]

output:
[1, 2, 1]

explaination:

The extracted text from the table is unclear. I'll reconstruct it manually based on the visible structure of the table:

---

### Explanation Table:

| Query No. | Action    | Generated Token | Timestamp | Expiry Timestamp | Unexpired Tokens |
|-----------|-----------|-----------------|-----------|------------------|------------------|
| 1         | Generate  | token1          | 3         | 38(3+35)         |                  |
| 2         | Count     | -               | 4         | -                | 1                |
| 3         | Generate  | token2          | 6         | 41(6+35)         |                  |
| 4         | Count     | -               | 7         | -                | 2                |
| 5         | Generate  | token3          | 11        | 46(11+35)        |                  |
| 6         | Count     | -               | 41        | -                | 1                |

"""


"""
Solution :
- We use hashmap to track the token


"""
from collections import defaultdict

def getUnexpiredToken(time_to_live, queries):
    dict_tokens =  defaultdict()
    output = []
    for query in queries:
        words_query = query.split(" ")
        if words_query[0] == "generate":
            dict_tokens[words_query[1]] = float(words_query[2]) + time_to_live
        elif words_query[0] == "renew":
            if words_query[1] in dict_tokens.keys():
                dict_tokens[words_query[1]] = float(words_query[2]) + time_to_live
        else:
            dict_tokens = {key: value for key,value in dict_tokens.items() if value - float(words_query[1]) > 0}
            count = len(dict_tokens.keys())
            output.append(count)

    return output


def main():
    # queries = ["generate token1 3", "count 4", "generate token2 6", "count 7", "generate token3 11", "count 41"]
    # time_to_live = 35
    time_to_live = 5
    queries = ["generate aaa 1", "renew aaa 2", "count 6", "generate bbb 7", "renew aaa 8", "renew bbb 10", "count 15"]
    print(getUnexpiredToken(time_to_live, queries))



if __name__ == "__main__":
    main()