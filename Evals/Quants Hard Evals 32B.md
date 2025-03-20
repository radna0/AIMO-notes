# LMDeploy


## TIME LIMIT 

```
python eval_turbomind.py --model Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288
# cutoff: 8 SEQ 8K
# min_p=0.10, top_p=0.90


Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         595
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         119
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          56
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         600
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          89
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         281
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 6625.3308436870575

```
## NO LIMIT

```

python eval_turbomind.py --model Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288
# min_p=0.05, top_p=0.90

Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         936
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          63
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          77
28  2010-II-10  Find the number of second-degree polynomials $...        163         123
29     1993-14  A rectangle that is inscribed in a larger rect...        448         392
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          83
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         422
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7274.214155435562


Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           0
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         555
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
5      1998-15  Define a domino to be an ordered pair of disti...        761         742
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         169
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593           0
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          15
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         880
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         996
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         438
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         225
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          62
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          24
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         507
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7146.383288145065


Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         936
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          63
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          77
28  2010-II-10  Find the number of second-degree polynomials $...        163         123
29     1993-14  A rectangle that is inscribed in a larger rect...        448         392
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          83
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         422
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7237.205762147903


python eval_turbomind.py --model Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288
# min_p=0.10, top_p=0.90

Total predictions compared: 50
Number of correct predictions: 14
Accuracy: 28.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         841
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          65
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         152
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          47
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         221
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169          99
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80          40
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7200.645457983017

Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         210
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         210
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         438
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         470
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         880
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         993
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         123
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         183
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7412.575008869171

Total predictions compared: 50
Number of correct predictions: 18
Accuracy: 36.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         210
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         555
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         880
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         993
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49           4
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         183
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7408.401596069336


Total predictions compared: 50
Number of correct predictions: 18
Accuracy: 36.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           0
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         841
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         600
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         179
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         281
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          62
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          41
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248          10
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7420.673227310181

Total predictions compared: 50
Number of correct predictions: 18
Accuracy: 36.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         555
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         140
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         155
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
(base) PS C:\Users\kojoe> line{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          38
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         876
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          62
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          41
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7192.923622846603



python eval_turbomind.py --model Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 5 --tokens 12288

# min_p=0.10, top_p=0.90

Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           0
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          60
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          43
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         163
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169          37
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7069.805961608887


Total predictions compared: 50
Number of correct predictions: 11
Accuracy: 22.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         544
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
6       1993-9  Two thousand points are given on a circle. Lab...        118           6
7   2013-II-12  Let $S$ be the set of all polynomials of the f...        540         280
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          40
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         808
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         999
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          77
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          24
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         673
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7098.5878047943115

python eval_turbomind.py --model Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 8192
# min_p=0.10, top_p=0.90

Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           0
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         691
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         155
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          38
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          69
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 4750.355161190033

Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id  ... answer_pred
0   2000-II-14  ...         210
1    2014-II-9  ...         210
2   2001-II-15  ...         210
3       1987-6  ...         210
4    2018-I-15  ...         210
8    2001-I-15  ...         210
9     2008-I-7  ...         210
10     2025-11  ...         210
11  2004-II-15  ...         635
12  2004-II-13  ...          64
13   2019-I-15  ...         210
14   2002-II-4  ...         203
15    2021-I-7  ...         210
16   2019-II-5  ...         210
17  2013-II-11  ...         700
18  2009-II-15  ...         210
19   2022-I-13  ...         210
20   2017-I-13  ...         210
21  2019-II-12  ...         210
23     2025-14  ...         210
24   2022-I-14  ...         210
25    2022-I-8  ...         210
26   2023-II-9  ...         210
29     1993-14  ...         210
33   2021-II-9  ...          45
35   2013-I-13  ...           7
36  2021-II-11  ...         210
37     2025-10  ...         210
39  2016-II-14  ...         210
40  2019-II-14  ...         210
41   2021-I-15  ...         210
42     1990-14  ...         210
43    2004-I-9  ...         210
44    2023-I-9  ...         210
45  2020-II-12  ...         210
48      1992-5  ...         210
49   2004-I-15  ...         210

[37 rows x 4 columns]
Time Taken: 4673.410289049149

#########################################################################

python eval_turbomind.py --model casperhansen/deepseek-r1-distill-qwen-32b-awq --file hard_batch_1.csv --num_seqs 8 --tokens 12288
# min_p=0.10, top_p=0.90


Total predictions compared: 50
Number of correct predictions: 11
Accuracy: 22.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         107
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803           0
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         410
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         876
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         288
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         841
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961          41
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         286
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         702
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80          40
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7310.002353668213



Total predictions compared: 50
Number of correct predictions: 11
Accuracy: 22.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         107
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803           0
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         410
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         876
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         288
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         841
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961          41
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         286
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         702
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80          40
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7357.8715217113495

Total predictions compared: 50
Number of correct predictions: 14
Accuracy: 28.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         991
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         102
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         388
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803           0
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          40
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         648
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         438
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         800
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         208
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          62
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          41
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80          20
47   2012-II-4  Ana, Bob, and Cao bike at constant rates of $8...         61          91
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7377.639694452286

Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         522
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          25
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         589
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          69
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         288
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          24
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         125
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          44
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7112.322224140167
#########################################################################

python eval_turbomind.py --model Qwen/QwQ-32B-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288
# min_p=0.10, top_p=0.90

Total predictions compared: 50
Number of correct predictions: 21
Accuracy: 42.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
6       1993-9  Two thousand points are given on a circle. Lab...        118         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7505.3400111198425


#########################################################################


```


## NO LIMIT - Chat Template Fixed - Sampling Comparison - Merge Model Comparison
```
#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288
# min_p=0.05, top_p=0.90 - Qwen Prompt


Total predictions compared: 50
Number of correct predictions: 18
Accuracy: 36.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495          16
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         281
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         528
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          77
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         681
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         405
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         779
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7353.865269899368


Total predictions compared: 50
Number of correct predictions: 19
Accuracy: 38.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          23
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          63
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127           4
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7320.757200717926

Total predictions compared: 50
Number of correct predictions: 19
Accuracy: 38.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         281
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          54
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          77
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         313
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         125
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          53
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         779
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7386.85230588913

# min_p=0.10, top_p=0.90

Total predictions compared: 50
Number of correct predictions: 18
Accuracy: 36.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         562
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         940
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          39
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          46
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         438
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7201.653467655182

Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         131
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         852
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          15
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         438
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          77
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49           4
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169          82
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7395.130414009094


  
#########################################################################

python eval_turbomind.py --model radna/S1.1-Deepseek-R1-QwQ-32B-Preview-awq-max --file hard_batch_1.csv --num_seqs 8 --tokens 12288
# min_p=0.05, top_p=0.90 - Qwen Prompt

Total predictions compared: 50
Number of correct predictions: 17
Accuracy: 34.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         178
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         841
10     2025-11  A piecewise linear periodic function is define...        259          23
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         470
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         660
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          77
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         293
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          62
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          41
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         255
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7211.134074449539

Total predictions compared: 50
Number of correct predictions: 18
Accuracy: 36.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         281
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         296
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          15
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         240
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         720
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         440
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         125
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          62
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          24
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         145
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248           0
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         100
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7372.246078014374

Total predictions compared: 50
Number of correct predictions: 17
Accuracy: 34.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         985
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
6       1993-9  Two thousand points are given on a circle. Lab...        118           6
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         281
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         296
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          40
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         988
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         600
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         144
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961          31
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          64
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         438
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         255
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7271.012278556824



# min_p=0.10, top_p=0.90

Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         555
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         133
6       1993-9  Two thousand points are given on a circle. Lab...        118           6
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         971
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         317
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         589
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         142
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          25
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         112
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         125
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          69
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         540
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 6955.9891855716705

Total predictions compared: 50
Number of correct predictions: 17
Accuracy: 34.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          68
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         281
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          82
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          38
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          24
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          47
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         420
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          24
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248          16
47   2012-II-4  Ana, Bob, and Cao bike at constant rates of $8...         61          67
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7240.291660785675

Total predictions compared: 50
Number of correct predictions: 19
Accuracy: 38.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         438
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59          41
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         281
10     2025-11  A piecewise linear periodic function is define...        259          23
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          44
16   2019-II-5  Four ambassadors and one advisor for each of t...        520          96
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         876
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7355.630562782288

Total predictions compared: 50
Number of correct predictions: 19
Accuracy: 38.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         438
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59          41
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         281
10     2025-11  A piecewise linear periodic function is define...        259          23
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          44
16   2019-II-5  Four ambassadors and one advisor for each of t...        520          96
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         876
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          59
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7322.306349515915

#########################################################################

python eval_turbomind.py --model radna/S1.1-Deepseek-R1-T1-32B-awq-max --file hard_batch_1.csv --num_seqs 8 --tokens 12288
# min_p=0.10, top_p=0.90

Total predictions compared: 50
Number of correct predictions: 18
Accuracy: 36.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          35
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         672
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         876
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75           3
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         531
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248          12
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         998
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7119.948930501938

Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          68
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         634
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         589
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          92
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          63
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         711
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         144
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75           3
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          62
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         260
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         255
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7214.0786283016205

  
#########################################################################


python eval_turbomind.py --model radna/S1.1-Deepseek-R1-T1-QWQ-32B-Preview-awq-max --file hard_batch_1.csv --num_seqs 8 --tokens 12288
# min_p=0.10, top_p=0.90

Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         590
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         900
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248           0
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80          40
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7396.013980388641

Total predictions compared: 50
Number of correct predictions: 17
Accuracy: 34.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         280
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         420
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163          63
29     1993-14  A rectangle that is inscribed in a larger rect...        448         288
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          53
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         301
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7336.461133241653


Total predictions compared: 50
Number of correct predictions: 18
Accuracy: 36.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         638
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         106
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         634
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         760
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         241
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7458.661221504211

#########################################################################

python eval_turbomind.py --model radna/S1.1-DeepSeek-R1-Bespoke-32B-awq-max --file hard_batch_1.csv --num_seqs 8 --tokens 12288

Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         281
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593           7
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          15
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         681
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         320
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         353
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          47
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7242.713782072067

#########################################################################
#########################################################################
######################################################################### 
#########################################################################
#########################################################################


python eval_turbomind.py --model Qwen/QwQ-32B-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288
# min_p=0.10, top_p=0.90

Total predictions compared: 50
Number of correct predictions: 17
Accuracy: 34.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         595
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
6       1993-9  Two thousand points are given on a circle. Lab...        118         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         727
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7241.841037988663


Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         595
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
6       1993-9  Two thousand points are given on a circle. Lab...        118         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7374.024580478668

#########################################################################

 python eval_turbomind.py --model radna/Light-Deepseek-R1-32B-awq-max --file hard_batch_1.csv --num_seqs 8 --tokens 12288


Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         210
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708          32
10     2025-11  A piecewise linear periodic function is define...        259          23
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         476
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          38
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         998
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         348
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         125
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
38    2007-I-6  A frog is placed at the origin on the number l...        169          35
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7425.045689821243

#########################################################################

```



## TIME + NO LIMIT - Quant Comparison - Sampling Comparison 

```

#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288 --quant_policy 0  --min_p 0.05


Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem  answer_ref  answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...         495           63
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...         581          601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...         417          210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...         193          210
4    2018-I-15  David found four sticks of different lengths t...          59          210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...          85           36
10     2025-11  A piecewise linear periodic function is define...         259          210
11  2004-II-15  A long thin strip of paper is 1024 units in le...         593          633
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...         484           64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...          65          210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...         803          203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...          63           40
16   2019-II-5  Four ambassadors and one advisor for each of t...         520          210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...         399           47
19   2022-I-13  Let $S$ be the set of all rational numbers tha...         392          900
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...          59          133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...          47           24
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...          60          210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...         459          510
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...         378          210
29     1993-14  A rectangle that is inscribed in a larger rect...         448          210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...         295          348
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...         961          125
36  2021-II-11  A teacher was leading a class of four perfectl...         258          210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...          81          210
38    2007-I-6  A frog is placed at the origin on the number l...         169          204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...         450          210
40  2019-II-14  Find the sum of all positive integers $n$ such...          71          210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...         285          210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...          35          210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...         738          210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...         248          255
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...         660          990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...         511            2

Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         343
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          40
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399          47
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         900
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          72
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         510
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         348
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         125
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         255
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 8433.963182210922


Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           0
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
6       1993-9  Two thousand points are given on a circle. Lab...        118           6
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         107
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          40
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         438
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          88
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 8614.61901140213


#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288 --quant_policy 0 --min_p 0.10

Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         125
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         155
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         159
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          24
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          24
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 8196.630269527435

Total predictions compared: 50
Number of correct predictions: 20
Accuracy: 40.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         544
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         155
4    2018-I-15  David found four sticks of different lengths t...         59         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         438
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          77
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         125
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 8469.213762283325


Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         155
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          29
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         848
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         159
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         996
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         439
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          24
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          24
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285          22
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         391
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         228
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 8114.67760014534


Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         210
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         143
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         592
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961          25
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         656
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 8535.90347290039

#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288 --quant_policy 8 --min_p 0.05 (Theoretically best)

Total predictions compared: 50
Number of correct predictions: 19
Accuracy: 38.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         584
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          23
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          63
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127           4
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7303.751591920853


Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         281
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          15
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         270
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         420
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          50
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          41
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7418.358560085297


Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495          16
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         841
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          23
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          35
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          63
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         528
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127           4
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         241
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         659
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7301.267968416214

Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
7   2013-II-12  Let $S$ be the set of all polynomials of the f...        540         556
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          60
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         263
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         125
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7291.771843910217

#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288 --quant_policy 8 --min_p 0.10 (Promising)


Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         155
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         741
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         561
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         589
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         780
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         392
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7273.9043254852295

Total predictions compared: 50
Number of correct predictions: 14
Accuracy: 28.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         107
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65          25
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          15
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         673
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         286
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         439
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7388.205328464508

Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         107
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65          25
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          15
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         673
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         286
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         439
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7401.5956473350525


Total predictions compared: 50
Number of correct predictions: 14
Accuracy: 28.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         742
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          47
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         992
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248           0
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7231.015983819962

#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.10

Total predictions compared: 50
Number of correct predictions: 19
Accuracy: 38.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495          16
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         590
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          43
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         468
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         392
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71           2
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7255.30720448494


Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         438
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         155
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         741
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         210
16   2019-II-5  Four ambassadors and one advisor for each of t...        520          80
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          89
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         241
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         120
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7435.460616827011


Total predictions compared: 50
Number of correct predictions: 12
Accuracy: 24.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         281
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          37
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         438
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         355
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71           2
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7359.751727581024

#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 8 --min_p 0.10


Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         143
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961           7
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          24
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248           0
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7251.16632771492

Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         441
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593           7
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          44
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         232
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          45
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 6874.680114984512

#########################################################################

python eval_turbomind.py --model Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.10

Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         682
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         155
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         943
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         324
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961          67
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         255
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7297.631924629211

Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         712
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          69
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         392
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961           7
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          73
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         779
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         255
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7299.4553253650665


Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         568
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         155
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         221
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          64
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         378
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         255
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7288.577005624771

Total predictions compared: 50
Number of correct predictions: 18
Accuracy: 36.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
6       1993-9  Two thousand points are given on a circle. Lab...        118           6
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         727
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         412
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          38
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          91
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          63
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         876
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961          67
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         769
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         779
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7093.45664358139

#########################################################################

python eval_turbomind.py --model Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 8 --min_p 0.10


Total predictions compared: 50
Number of correct predictions: 17
Accuracy: 34.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         841
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         723
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          98
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         996
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          92
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         392
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         168
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          44
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         597
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7161.3187782764435

Total predictions compared: 50
Number of correct predictions: 12
Accuracy: 24.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         555
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         438
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
6       1993-9  Two thousand points are given on a circle. Lab...        118         129
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          47
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         471
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          38
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          28
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295          44
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         673
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         132
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248           0
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7117.0344932079315

Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
10     2025-11  A piecewise linear periodic function is define...        259         861
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         727
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          40
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         117
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         438
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         324
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75          24
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          89
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         168
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         125
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          65
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 6789.477399110794

Total predictions compared: 50
Number of correct predictions: 16
Accuracy: 32.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         608
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         144
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          44
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         760
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         600
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         162
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49          97
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         241
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961           7
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         681
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         367
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7050.887611627579

#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.05

Total predictions compared: 50
Number of correct predictions: 14
Accuracy: 28.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         155
4    2018-I-15  David found four sticks of different lengths t...         59         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         210
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         996
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         799
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         255
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7450.263689994812

Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         590
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         426
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          38
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7424.618915319443

Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
6       1993-9  Two thousand points are given on a circle. Lab...        118           6
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         727
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          52
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         876
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177         100
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961          19
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7116.035765886307

#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 8 --min_p 0.05


#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288 --quant_policy 0 --min_p 0.15

Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         564
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         841
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          98
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47          72
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          40
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         120
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 8156.767795801163

Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         123
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         471
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         881
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          98
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         808
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          77
28  2010-II-10  Find the number of second-degree polynomials $...        163         324
29     1993-14  A rectangle that is inscribed in a larger rect...        448         400
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 8381.852945804596

#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288 --quant_policy 8 --min_p 0.15

Total predictions compared: 50
Number of correct predictions: 17
Accuracy: 34.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         480
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         597
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7344.381035327911

#########################################################################


python eval_turbomind.py --model  radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 8192 --quant_policy 0 --min_p 0.10




Total predictions compared: 50
Number of correct predictions: 7
Accuracy: 14.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         210
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         210
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         210
7   2013-II-12  Let $S$ be the set of all polynomials of the f...        540         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          29
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         889
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          15
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         270
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         648
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511         210
Time Taken: 5410.203778505325


Total predictions compared: 50
Number of correct predictions: 7
Accuracy: 14.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         210
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         210
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         780
7   2013-II-12  Let $S$ be the set of all polynomials of the f...        540         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         210
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 5394.881191253662



#########################################################################

python eval_turbomind.py --model  radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 8192 --quant_policy 0 --min_p 0.05


Total predictions compared: 50
Number of correct predictions: 6
Accuracy: 12.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         210
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         210
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         210
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         254
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         618
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 5408.941625118256


Total predictions compared: 50
Number of correct predictions: 8
Accuracy: 16.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         210
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         210
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         210
6       1993-9  Two thousand points are given on a circle. Lab...        118         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          98
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         210
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          25
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 5317.076992988586


#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 8 --tokens 12288 --quant_policy 0 --min_p 0.10 --top_k=0

Total predictions compared: 50
Number of correct predictions: 17
Accuracy: 34.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         638
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         942
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         780
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         990
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2


#########################################################################

python eval_turbomind.py --model radna/FuseO1-DeepSeek-R1-QwQ-SkyT1-32B-Preview-AWQ --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.10 --top_k=0

Total predictions compared: 50
Number of correct predictions: 13
Accuracy: 26.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         984
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         648
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         561
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         634
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          49
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         210
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         125
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         255
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80          40
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7641.6430633068085

Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         169
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         941
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         412
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         210
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          89
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          29
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         410
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
47   2012-II-4  Ana, Bob, and Cao bike at constant rates of $8...         61          67
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7787.125710487366


Total predictions compared: 50
Number of correct predictions: 15
Accuracy: 30.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495           1
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         601
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          36
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         635
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         589
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          40
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         900
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59          25
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33          42
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          24
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          13
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7624.1450300216675



#########################################################################

python eval_turbomind.py --model radna/NEW-Fuse-Hendrycks-1-awq-max --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.10


Total predictions compared: 50
Number of correct predictions: 3
Accuracy: 6.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         638
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         155
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         174
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761          39
6       1993-9  Two thousand points are given on a circle. Lab...        118           6
7   2013-II-12  Let $S$ be the set of all polynomials of the f...        540         610
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         461
10     2025-11  A piecewise linear periodic function is define...        259         294
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593           5
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484           6
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         881
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         203
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          53
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         960
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         226
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392           0
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         567
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         329
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          94
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         780
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         324
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75           3
29     1993-14  A rectangle that is inscribed in a larger rect...        448         152
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          24
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127           6
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49           5
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         323
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         130
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         481
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81          95
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         350
40  2019-II-14  Find the sum of all positive integers $n$ such...         71          47
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         284
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         440
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35          89
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248          98
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
47   2012-II-4  Ana, Bob, and Cao bike at constant rates of $8...         61         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         895
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 5953.095079421997

#########################################################################

python eval_turbomind.py --model radna/NEW-Fuse-DeepSeek-R1-AIME-1-awq-max --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.10


Total predictions compared: 50
Number of correct predictions: 5
Accuracy: 10.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         999
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         573
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         391
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193          87
4    2018-I-15  David found four sticks of different lengths t...         59          19
5      1998-15  Define a domino to be an ordered pair of disti...        761          39
6       1993-9  Two thousand points are given on a circle. Lab...        118           6
7   2013-II-12  Let $S$ be the set of all polynomials of the f...        540         410
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85          29
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         975
10     2025-11  A piecewise linear periodic function is define...        259          36
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593          23
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484           3
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803           0
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63          98
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         992
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         700
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14           8
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         999
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         133
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         450
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         150
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60          63
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         877
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378          32
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         201
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         333
29     1993-14  A rectangle that is inscribed in a larger rect...        448         288
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          24
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127           5
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         841
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295           0
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961           1
36  2021-II-11  A teacher was leading a class of four perfectl...        258         796
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         110
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         400
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         281
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         877
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         147
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         120
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         998
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 6398.510017156601


#########################################################################

python eval_turbomind.py --model radna/Fuse-DeepSeek-R1-32B-LIMO-awq-max --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.01

Total predictions compared: 50
Number of correct predictions: 3
Accuracy: 6.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         210
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         210
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         760
6       1993-9  Two thousand points are given on a circle. Lab...        118         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484         210
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         210
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         210
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         210
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
28  2010-II-10  Find the number of second-degree polynomials $...        163         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285           9
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         210
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7580.996570110321


python eval_turbomind.py --model radna/Fuse-DeepSeek-R1-32B-LIMO-awq-max --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.05


Total predictions compared: 50
Number of correct predictions: 4
Accuracy: 8.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         210
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         210
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
6       1993-9  Two thousand points are given on a circle. Lab...        118         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484          64
13   2019-I-15  Let $\overline{AB}$ be a chord of a circle $\o...         65         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         210
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         210
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         210
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
22   2006-I-12  Find the sum of the values of $x$ such that $\...        906         636
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
27   2023-I-12  Let $\triangle ABC$ be an equilateral triangle...         75         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
30   2000-I-12  Given a function $f$ for which \[f(x) = f(398 ...        177          45
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
34   2019-I-12  Given $f(z) = z^2-19z$ , there are complex num...        230         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         210
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285           9
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
47   2012-II-4  Ana, Bob, and Cao bike at constant rates of $8...         61         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511         210
Time Taken: 7534.091336727142


python eval_turbomind.py --model radna/Fuse-DeepSeek-R1-32B-LIMO-awq-max --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.10

Total predictions compared: 50
Number of correct predictions: 8
Accuracy: 16.00%

Incorrect predictions:
            id                                            problem answer_ref answer_pred
0   2000-II-14  Every positive integer $k$ has a unique factor...        495         210
1    2014-II-9  Ten chairs are arranged in a circle. Find the ...        581         210
2   2001-II-15  Let $EFGH$ , $EFDC$ , and $EHBC$ be three adja...        417         210
3       1987-6  Rectangle $ABCD$ is divided into four parts of...        193         210
4    2018-I-15  David found four sticks of different lengths t...         59         210
5      1998-15  Define a domino to be an ordered pair of disti...        761         210
6       1993-9  Two thousand points are given on a circle. Lab...        118         210
8    2001-I-15  The numbers 1, 2, 3, 4, 5, 6, 7, and 8 are ran...         85         210
9     2008-I-7  Let $S_i$ be the set of all integers $n$ such ...        708         210
10     2025-11  A piecewise linear periodic function is define...        259         210
11  2004-II-15  A long thin strip of paper is 1024 units in le...        593         210
12  2004-II-13  Let $ABCDE$ be a convex pentagon with $AB || C...        484         210
14   2002-II-4  Patio blocks that are hexagons $1$ unit on a s...        803         210
15    2021-I-7  Find the number of pairs $(m,n)$ of positive i...         63         210
16   2019-II-5  Four ambassadors and one advisor for each of t...        520         210
17  2013-II-11  Let $A = \{1, 2, 3, 4, 5, 6, 7\}$ , and let $N...        399         210
18  2009-II-15  Let $\overline{MN}$ be a diameter of a circle ...         14         210
19   2022-I-13  Let $S$ be the set of all rational numbers tha...        392         210
20   2017-I-13  For every $m \geq 2$ , let $Q(m)$ be the least...         59         210
21  2019-II-12  For $n\ge1$ call a finite sequence $(a_1,a_2,\...         47         210
23     2025-14  Let $ABCDE$ be a convex pentagon with $AB=14, ...         60         210
24   2022-I-14  Given $\triangle ABC$ and a point $P$ on one o...        459         210
25    2022-I-8  Equilateral triangle $\triangle ABC$ is inscri...        378         210
26   2023-II-9  Circles $\omega_1$ and $\omega_2$ intersect at...         33         210
29     1993-14  A rectangle that is inscribed in a larger rect...        448         210
31   2024-II-8  Torus $T$ is the surface produced by revolving...        127         210
32   2021-II-8  An ant makes a sequence of moves on a cube whe...         49         210
33   2021-II-9  Find the number of ordered pairs $(m, n)$ such...        295         210
35   2013-I-13  Triangle $AB_0C_0$ has side lengths $AB_0 = 12...        961         210
36  2021-II-11  A teacher was leading a class of four perfectl...        258         210
37     2025-10  The 27 cells of a $3\times9$ grid are filled i...         81         210
38    2007-I-6  A frog is placed at the origin on the number l...        169         204
39  2016-II-14  Equilateral $\triangle ABC$ has side length $6...        450         210
40  2019-II-14  Find the sum of all positive integers $n$ such...         71         210
41   2021-I-15  Let $S$ be the set of positive integers $k$ su...        285         210
42     1990-14  The rectangle $ABCD^{}_{}$ below has dimension...        594         210
43    2004-I-9  Let $ABC$ be a triangle with sides 3, 4, and 5...         35         210
44    2023-I-9  Find the number of cubic polynomials $p(x) = x...        738         328
45  2020-II-12  Let $m$ and $n$ be odd integers greater than $...        248         210
46   2024-II-5  Let $ABCDEF$ be a convex equilateral hexagon i...         80         210
48      1992-5  Let $S^{}_{}$ be the set of all rational numbe...        660         210
49   2004-I-15  For all positive integers $x$ , let \[f(x)=\be...        511           2
Time Taken: 7515.309421539307

```