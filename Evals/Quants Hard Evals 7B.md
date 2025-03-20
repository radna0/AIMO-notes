

```

python eval_turbomind.py --model casperhansen/deepseek-r1-distill-qwen-7b-awq --file hard_batch_1.csv --num_seqs 32 --tokens 12288 --quant_policy 0 --min_p 0.05

Total predictions compared: 50
Number of correct predictions: 7
Accuracy: 14.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         390
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59          11
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
6       1993-9  Two thousand points are given on a circle. Lab...        118           6
7   2013-II-12  Let $S$ be the set of all polynomials of the f...        540         556
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259          36
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         470
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         455
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          98
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         680
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         999
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         504
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         201
28  2010-II-10  Find the number of second-degree polynomials $...        163         324
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177         352
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         841
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          76
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         350
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          24
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         702
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         167
47   2012-II-4  Ana, Bob, and Cao bike at constant rates of $8...         61          50
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 4247.0381100177765


python eval_turbomind.py --model casperhansen/deepseek-r1-distill-qwen-7b-awq --file hard_batch_1.csv --num_seqs 32 --tokens 12288 --quant_policy 0 --min_p 0.10



Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         390
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59          29
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
7   2013-II-12  Let $S$ be the set of all polynomials of the f...        540         556
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259          23
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         680
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         999
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          49
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         518
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          40
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         288
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177         176
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127           7
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         620
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          95
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71           2
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         599
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         255
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 4176.803159236908


######################################################################

python eval_turbomind.py --model casperhansen/deepseek-r1-distill-qwen-7b-awq --file hard_batch_1.csv --num_seqs 48 --tokens 12288 --quant_policy 0 --min_p 0.05

python eval_turbomind.py --model casperhansen/deepseek-r1-distill-qwen-7b-awq --file hard_batch_1.csv --num_seqs 48 --tokens 12288 --quant_policy 0 --min_p 0.10

Total predictions compared: 50
Number of correct predictions: 11
Accuracy: 22.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         178
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
7   2013-II-12  Let $S$ be the set of all polynomials of the f...        540         556
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         343
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593           0
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          15
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         760
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         999
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          39
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         438
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         625
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         288
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127          86
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         841
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         673
36  2021-II-11  A teacher was leading a class of four perfectl...        258          70
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          78
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          24
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         801
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         598
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248           0
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 5475.771462440491

python eval_turbomind.py --model casperhansen/deepseek-r1-distill-qwen-7b-awq --file hard_batch_1.csv --num_seqs 48 --tokens 12288 --quant_policy 0 --min_p 0.15


Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           0
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         432
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708           1
10     2025-11  A piecewise linear periodic function is define...        259          23
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          98
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         720
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          44
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         111
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          27
28  2010-II-10  Find the number of second-degree polynomials $...        163         324
29     1993-14  A rectangle that is inscribed in a larger rect...        448         288
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          24
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127           7
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         841
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961           7
36  2021-II-11  A teacher was leading a class of four perfectl...        258         678
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          44
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          24
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         702
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248           0
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 5399.525772809982


######################################################################


python eval_turbomind.py --model casperhansen/deepseek-r1-distill-qwen-7b-awq --file hard_batch_1.csv --num_seqs 32 --tokens 16384 --quant_policy 0 --min_p 0.05


python eval_turbomind.py --model casperhansen/deepseek-r1-distill-qwen-7b-awq --file hard_batch_1.csv --num_seqs 32 --tokens 16384 --quant_policy 0 --min_p 0.10

Total predictions compared: 50
Number of correct predictions: 7
Accuracy: 14.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         395
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
7   2013-II-12  Let $S$ be the set of all polynomials of the f...        540          52
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         343
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593           0
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         680
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         999
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          40
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75          25
28  2010-II-10  Find the number of second-degree polynomials $...        163         324
29     1993-14  A rectangle that is inscribed in a larger rect...        448         288
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          24
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127          23
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         841
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         673
36  2021-II-11  A teacher was leading a class of four perfectl...        258          37
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          20
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71           2
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         234
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          55
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 4192.972040891647




######################################################################

python eval_turbomind.py --model arcee-ai/Arcee-Maestro-7B-Preview-AWQ --file hard_batch_1.csv --num_seqs 32 --tokens 16384 --quant_policy 0 --min_p 0.05

Total predictions compared: 50
Number of correct predictions: 8
Accuracy: 16.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         174
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59           3
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259          23
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         470
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          98
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         720
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          92
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          39
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          63
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         638
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         324
29     1993-14  A rectangle that is inscribed in a larger rect...        448         288
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177         352
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         223
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         841
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961           1
36  2021-II-11  A teacher was leading a class of four perfectl...        258         137
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          78
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         350
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          52
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248           0
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 4606.333122968674

python eval_turbomind.py --model arcee-ai/Arcee-Maestro-7B-Preview-AWQ --file hard_batch_1.csv --num_seqs 32 --tokens 12288 --quant_policy 0 --min_p 0.10

Total predictions compared: 50
Number of correct predictions: 9
Accuracy: 18.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         432
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         309
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         470
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         485
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          15
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         760
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         117
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          22
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         474
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         324
29     1993-14  A rectangle that is inscribed in a larger rect...        448         392
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          24
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127           7
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         841
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         231
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961           1
36  2021-II-11  A teacher was leading a class of four perfectl...        258         399
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          84
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         350
40  2019-II-14  Find the sum of all positive integers $n$ such...         71           2
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         324
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248           0
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 4659.169843673706


python eval_turbomind.py --model arcee-ai/Arcee-Maestro-7B-Preview-AWQ --file hard_batch_1.csv --num_seqs 32 --tokens 12288 --quant_policy 0 --min_p 0.10  --top_k=0


Total predictions compared: 50
Number of correct predictions: 8
Accuracy: 16.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         257
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
5      1998-15  Define a domino to be an ordered pair of disti...        761         560
6       1993-9  Two thousand points are given on a circle. Lab...        118           6
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259          23
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         470
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         379
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         760
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         203
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          30
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          42
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         657
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         324
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177         352
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127           7
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         841
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         673
36  2021-II-11  A teacher was leading a class of four perfectl...        258          99
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          69
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         100
40  2019-II-14  Find the sum of all positive integers $n$ such...         71           6
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         234
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248           1
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 5127.7542543411255

######################################################################

python eval_turbomind.py --model arcee-ai/Arcee-Maestro-7B-Preview-AWQ --file hard_batch_1.csv --num_seqs 48 --tokens 12288 --quant_policy 0 --min_p 0.10  --top_k=0/-1


Total predictions compared: 50
Number of correct predictions: 8
Accuracy: 16.00%
Time Taken: 6389.110677242279

######################################################################


python eval.py --model arcee-ai/Arcee-Maestro-7B-Preview-AWQ --file hard_batch_1.csv --num_seqs 32 --tokens 12288 --quant_policy 0 --min_p 0.05  --top_k=0/-1

# 2 Times

Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%
Time Taken: 9246.15100312233


python eval_turbomind.py --model arcee-ai/Arcee-Maestro-7B-Preview-AWQ --file hard_batch_1.csv --num_seqs 32 --tokens 12288 --quant_policy 0 --min_p 0.05  --top_k=0/-1

Total predictions compared: 50
Number of correct predictions: 7
Accuracy: 14.00%
Time Taken: 9233.610472679138


# 2 Times

Total predictions compared: 50
Number of correct predictions: 8
Accuracy: 16.00%
Time Taken: 9248.153326034546



Total predictions compared: 50
Number of correct predictions: 11
Accuracy: 22.00%
Time Taken: 9281.103632450104

```