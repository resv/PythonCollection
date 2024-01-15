--------   Unit testing | from <function name> import <filename where function written>   --------------------------------------------------------------------------------------------------------------------------

-------- WRITING UNIT TESTING --------------------------------------------------------------------------------------------------------------------------
from rearrange import rearrange_name 
import unittest

class TestRearrange (unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)  #yes testcase is not camel case even though in class above
unittest.main()

--------  EDGE CASES    --------------------------------------------------------------------------------------------------------------------------

--------  RAISE ValueErrors    --------------------------------------------------------------------------------------------------------------------------
def validate_user(username, minlen):
    if minlen &lt; 1:
        raise ValueError("minlen must be at least 1") 
    
    if len(username) < minlen:
    return False

    if not username.isalnum():
        return False
    return True
I
--------  ASSERT ValueErrors  ( CHECKS conditional values are correct like str and int)   -------------------------------------------------------
def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

-------- TRY-EXCEPT    ------------------------------------------------------------
def character_frequency(filename):
***Counts the frequency of each character in the given file."" # First try to open the file
    try:
        f = open(filename)
    except OSError:
        return None
    
    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] characters.get(char, 0) + 1
    f.close()c
    return characters


--------   Example of test and Raise assert   --------------------------------------------------------------------------------------------------------------------------
import unittest

from validations import validate_user

class TestValidateUser (unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user(&quot;validuser&quot;, 3), True)

    def test_too_short(self):
        self.assertEqual (validate_user(&quot;inv&quot;, 5), False)

    def test_invalid_characters (self):
        self.assertEqual (validate_user(&quot;invalid_user&quot;, 1), False)

    def test_invalid_minlen(self):
        self.assertRaises (ValueError, validate_user, &quot;user&quot;, -1)
# Run the tests 
unittest.main()
--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------

--------      --------------------------------------------------------------------------------------------------------------------------


