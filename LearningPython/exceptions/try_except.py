# Exceptions

# keywords: try and except

# All non-system-exiting exceptions are derived from the Exception class

# Ex of hierarchy

# BaseException
# +--SystemExit
# +--KeyboardInterrupt
# +--Exception
    # +--ArithmeticError
        # +--FloatingPointError
        # +--OverflowError
        # +--ZeroDivisionError   
#...

# Concept

# try:
#   Protected code that might trigger an exception
# except:
#   Handle exception properly
# else:
#   Only when no exceptions
# finally:
#   Always run this code


