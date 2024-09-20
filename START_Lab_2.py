def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    
    def is_palindrome(s):
        s = s.replace(" ", "").lower()
        return s == s[::-1] 
    return is_palindrome(word)
    

def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    def fib_up_to(num):
        fib_seq = []
        count = 0
        number = 1
        f1 = 0
        f2 = 1

        if num >= 0:
            fib_seq = [0, 1]
            while True:
                next_fib = fib_seq[-1] + fib_seq[-2]
                if next_fib > num:
                    break
                fib_seq.append(next_fib)
            return fib_seq
        else:
            return fib_seq
    return fib_up_to(number_val)


def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    def count_string(str1, str2):
        str1_low = str1.lower()
        return str1.count(str2)
    return count_string(str1, str2)


def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    pass

    return sum_list

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = None

    return password

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    pass

