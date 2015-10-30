#runs 10 times
n = 10

def endLine():
    print "*" + " "*(n+1) + "*"

endLine()
for i in range(n):
    # prints an 'N'
    print "*" + " "*i + "*" + " "*(n-i) + "  *"
endLine()