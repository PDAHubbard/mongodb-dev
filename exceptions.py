# Exceptions, caught and uncaught
import sys

try:
    print 5 / 0
except Exception as e:
    print "Exception :-> ", type(e), e

print "Life goes on."

print 5/0
