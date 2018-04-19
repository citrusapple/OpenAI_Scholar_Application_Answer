# this uses the append method, so once you hit z itll keep going?

from string import ascii_lowercase


def extract(query):
    """extract takes in a `query` API function
    (which returns the first 5 usernames, lexicographically sorted,
    that start with a prefix) and returns the sorted list of
    all usernames in the database.

    For example, the `query` function in provided in `main`
    works as follows:

    query("a") #=> ["abracadara", "al", "alice", "alicia", "allen"]
    query("ab") #=> ["abracadara"]

    The following implementation would pass the assertion in `main`,
    but is not a correct solution since it
    works only for that example `query`:

    def extract(query):
        return query("ab") + query("al") + query("altercation")
        + query("b") + query("el") + query("ev") + query("m")

# so like here we would say query = ['ab','al','altercation',''b','el',]
# and then pass query into def extract(query)
    Your goal is to write an `extract` method that is correct
    for any provided `query`.
    """

    number = 1  # to keep track of the number of characters in the prefix we are testing
    alpha = list(ascii_lowercase)  # list of a-z to iterate through
    answer = set()  # empty set for input in our recursive function
    def recursive(x, holder, num, char):
        #temp holds query(x) so the code doesn't have to keep running query()
        temp = query(x)
        #if query(x) returns less than 5 we can stop looking for that prefix and move on to the next in alphabet
        if len(temp) < 5:
            if list(x)[-1] != "z":
                # if the last character of our prefix input is not z, we can look for the next character in alpha
                ind = alpha.index(list(x)[-1])
                #find the index of our last character
                holder = set(temp) | holder
                #store our results so far into holder
                new = "".join(list(x)[:-1]) + alpha[ind + 1]
                #find the next character and add it to the letters before
                if num > 1:
                    #if we're at single characters i.e. "a", we don't have to do anything to num
                    num -= 1
                    #otherwise, we want to subtract one character in num or we will go into an infinite loop
                return recursive(new, holder, num, alpha[ind:])
                #use our new prefix and put it through the function again
            else:
                #if our input x is actually "z"/ ends with "z"
                if len(temp) < 5:
                    #store whatever it yileds
                    holder = set(temp) | holder
                    if len(x) != 1:
                        #if it's not "z" but just ends with "z"
                        ind = (alpha.index(list(x)[-2])) + 1
                        new = "".join(list(x)[:-2]) + alpha[ind]
                        num -= 1
                        return recursive(new, holder, num, alpha[ind + 1:])
                        #we go back to the character before and look for the next. ie if "alz",next is "am"
                    else:
                        #if we're at "z", just return everything, this is our base case
                        return holder
                #if it does return with 5 results
                else:
                    holder = set(temp) | holder
                    #and it's not single "z"
                    if len(x) != 1:
                        num += 1
                        new = "".join(last[0:num])
                        ind = alpha.index(last[num])
                        return recursive(new, holder, num, alpha[ind:])
                        #we'll go back to the character before this
                    else:
                        #otherwise we're done, return our stored results
                        return holder
        #if query(x) yields 5 results
        elif len(temp) == 5:
            holder = set(temp) | holder
            last = list(temp[4])
            num += 1
            new = "".join(last[0:num])
            ind = alpha.index(last[num-1])
            #we store the value, look at the last word and the prefix with one extra character and run it again!
            return recursive(new, holder, num, alpha[ind:])
        #return all of our stored values in holder
        return holder

    final = recursive("a", answer, number, alpha)
    return sorted(list(final))
    #since we've been storing everything in sets, we have to make it into a list and sort before returning.


def main():
    """Runs your solution -- no need to update (except to maybe try out different databases)."""
    # Sample implementation of the autocomplete API
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]

    print("test case 1: assigned list")
    database = sorted([
        "abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "eve", "evening", "event",
        "eventually", "mallory"
    ])
    assert extract(query) == database
    print("Passed! Evolution: Pichu")
    print("\r")

    print("test case 2: lots of 'username + a-z'")
    database = ['usernamea', 'usernameb', 'usernamec', 'usernamed', 'usernamee', 'usernamef', 'usernameg', 'usernameh', 'usernamei', 'usernamej', 'usernamek', 'usernamel', 'usernamem', 'usernamen', 'usernameo', 'usernamep', 'usernameq', 'usernamer', 'usernames', 'usernamet', 'usernameu', 'usernamev', 'usernamew', 'usernamex', 'usernamey', 'usernamez']
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database
    print("Passed! Evolution: Pikachu")
    print("\r")

    print("test case 3: empty")
    database = sorted([
    ])
    assert extract(query) == database
    print("Passed! Evolution: Raichu")




main()

