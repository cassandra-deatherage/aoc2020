print("hello world")
input = """1652
1998
1677
1855
1955
1875
1993
1860
1752
1936
1816
1924
1872
2000
1967
1882
1737
1801
1832
1985
1933
1911
1894
1384
1871
1607
1858
1950
222
1931
1635
1960
1909
1884
1921
1959
1981
1920
1684
1734
1490
1632
1935
1982
217
1874
1646
1943
986
1509
1899
1834
1908
1769
1989
1977
1436
1973
1974
1941
1624
2006
1867
843
2003
1838
1904
1892
1972
1957
1890
1540
1578
1845
1912
1947
1847
1841
1793
2005
1716
1852
1865
1532
1800
1949
1898
1698
1806
1840
1833
1915
479
1963
1923
1567
1849
1536
1741
1818
1934
1952
1805
1868
1808
955
1954
1712
1797
1472
1807
1673
1601
1883
1869
1969
1886
1491
1572
2010
1796
1870
1946
1938
1813
1825
1944
129
1856
1827
1939
1642
1542
745
1836
1810
529
1822
1917
486
1953
2008
1991
1628
1937
1987
1837
1820
1922
1850
1893
1942
1928
1990
1589
1970
1986
1925
1902
2009
1565
1610
1857
1889
1901
1790
1880
1999
1964
1948
1824
1877
1916
1978
1839
1659
1846
323
1387
1926
1958
1914
1906
178
1979
1994
2004
1862
1704
1903
1997
1876
1992
1864
1932
1918
1962
1802
1278
1861"""

#create an array of the numbers
nums = []
for line in input.splitlines():
    x = int(line)
    nums.append(x)

print(nums)
#subtract the first number from 2020
#check the rest in the range to see if they are the equivalent
#if they are then print and exit
def part1(nums):
    for i in range(len(nums)):
        x = nums[i]
        difference = 2020 - nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == difference:
                print(f"x = {x} j = {nums[j]}")
                answer = x * nums[j]
                print (answer)

                return answer

#call the function
part1(nums)

#find the three numbers that sum to 2020
def part2(nums):
    for i in range(len(nums)):
        a = nums[i]
        difference_a = 2020 - nums[i]
        for j in range(i+1, len(nums)):
            b = nums[j]
            difference_b = 2020 - nums[j]
            for k in range(i+2, len(nums)):
                c = nums[k]
                if a+b+c == 2020:
                    print(f"a ={a} b ={nums[j]} c ={nums[k]}")
                    sum = a+b+c
                    print (sum)

                    #find the product of the three numbers
                    product = a * b * c
                    print (product)
                    return product
#call the function
part2(nums)


