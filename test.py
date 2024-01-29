k, b = map(input().count, "kb")
print(("none", ("bo", "ki")[b < k] + ("ki", "ba")[k < b])[b + k > 0])

def foo(data):
    k, b = map(data.count, "kb")
    data = ("none", ("bo", "ki")[b < k] + ("ki", "ba")[k < b])[b + k > 0]
    return data


tests = (
    ("boba", "boba"),
    ("kiki", "kiki"),
    ("kobra", "boki"),
    ("ljus", "none"),
)
for data, res in tests:
    ret_data = foo(data)
    assert ret_data == res

tests = (0, 0, "none"), (2, 2, "boki"), (3, 1, "boba"), (1, 3, "kiki")

lambda n: "nonekikiboba"[n*2:][:4]

"""
boba
kiki
boki

"""
"kbiokbia"
# b + k == 0 => 0
# k > b => 2
# k == b => 3
# b > k => 4

# (b + k != 0) * 2
# b >= k
# 
# print(("none", "boki", "boba", "kiki")[(b + k != 0) + (b > k) + (k > b) * 2])

out = []
for b, k, res in ((0, 0, "none"), (2, 2, "boki"), (3, 1, "boba"), (1, 3, "kiki")):
    ans = ("none", ("ki", "bo")[b >= k] + ("ba", "ki")[k >= b])[b + k != 0]
    ans1 = ("none", ("bo", "ki")[b < k] + ("ki", "ba")[k < b])[b + k != 0]
    out.append([ans, ans1, res])
    # assert ("none", "boki", "boba", "kiki")[(b_1 + k_1 != 0) + (b_1 > k_1) + (k_1 > b_1) * 2] == res
print(out)    


