"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""
def resource(AnyString):
    trans = str.maketrans('','','aeiouAEIOU')
    return string[0] + string[1:].translate(trans)
