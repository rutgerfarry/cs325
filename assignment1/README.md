# assignment1
- Rutger Farry
- CS325
- Dr. Xiaoli Fern
- 31 January 2016

## Running the code
The scripts are built in Python 2, so running them should be simple on most computers:
```
python bruteforce.py example.input
python divideandconquer.py example.input
python enhanceddnc.py example.input
```

To run performance tests just do:
```
python profiler.py
```

## Pseudocode
Brute-force:
```
min_distance = infinity
for i = 1 to len(P) - 1
  for j = i + 1 to len(P)
    let p = P[i], q = P[j]
    if distance(p, q) < min_distance:
      min_distance = dist(p, q)
      closestPair = (p, q)
return closestPair
```

Divide and Conquer:
```
min_distance = infinity

closest_pair(P):
  if len(P) <= 3:
    recursive case, return closest closest_pair
  sort P by x-value
  median = P[len(P) / 2]
  left_set = left(P)
  right_set = right(P)
  min_distance = min(closest_pair(left_set), closest_pair(right_set))
  middle_set = points within min_distance of median(P)
  return closest_cross_pair(middle_set)

closest_cross_pair(P):
  sort P by y-value
  for i = 0...len(P):
    for j = i+1...len(P):
      break if P[j] - P[i] > min_distance
      min_distance = min(distance(P[i], P[j], min_distance))
  return min_distance
```

Enhanced Divide and Conquer:
```
min_distance = infinity
x_P = sort P by x-value
y_P = sort P by y-value

closest_pair(x_P, y_P):
  if len(x_P) <= 3:
    recursive case, return closest closest_pair
  median = x_P[len(x_P) / 2]
  x_left_set = left(x_P)
  x_right_set = right(x_P)
  y_left_set = intersection of x_left_set and y_P
  y_right_set = intersection of x_right_set and y_P

  min_distance = min(
    closest_pair(x_left_set, y_left_set), 
    closest_pair(x_right_set, y_right_set))
  middle_set = points plucked from y_sorted_points within min_distance of median(P)
  return closest_cross_pair(middle_set)

closest_cross_pair(P):
  for i = 0...len(P):
    for j = i+1...len(P):
      break if P[j] - P[i] > min_distance
      min_distance = min(distance(P[i], P[j], min_distance))
  return min_distance
```

## Asymptotic Analysis of Runtime
The recursive relation for the naïve divide and conquer algorithm is: *T(n) = 2 T(n/2) + cn log(n)*, which gives us a runtime of *O(n log^2 n)*.

The recursive relation for the enhanced divide and conquer algorithm, however is *T(n) = 2 T(n/2) + cn*, giving us a runtime of only *O(n log n)*, a pretty decent improvement.

## Profiler Output
I wrote a small profiler script that prints the runtimes of the three algorithms. Here's the output of a run whose data is used for the chart below:
```
PROFILER ___________________________________________
bruteforce took 0.0228321552277s for input of size 10^2
divideandconquer took 0.00112295150757s for input of size 10^2
enhanceddnc took 0.0015549659729s for input of size 10^2


bruteforce took 2.33831596375s for input of size 10^3
divideandconquer took 0.0186910629272s for input of size 10^3
enhanceddnc took 0.0779881477356s for input of size 10^3


bruteforce took 360.704819202s for input of size 10^4
divideandconquer took 0.235679149628s for input of size 10^4
enhanceddnc took 5.21158695221s for input of size 10^4


divideandconquer took 3.02355504036s for input of size 10^5
enhanceddnc took 1287.88584304s for input of size 10^5


divideandconquer took 56.5322129726s for input of size 10^6
```

## Plotting the Runtime
![alt](https://lh5.googleusercontent.com/7GPOSd-v5f91zhs48zDUlYNjgyyAg98lLorvqPZ8ZdPAS83AgezMwptTgOP0qLkYrzfwHvu8id44tao=w2880-h1564)

## Interpratation and discussion
I was suprised to see how long the enhanced divide and conquer algorithm took on my computer. I spent some time debugging to ensure the list was shrinking with each recursive call. It was. Despite seemingly implementing the algorithm correctly, it seems that the compare step for intersecting the chosen x points with the master sorted y list took much longer than *O(n)*. 

Additionally, I originally built the functions to just return the distance between the two shortest points, meaning I was unable to add the ability to output all sets of closest points within the time limit, opting to just output one set instead. (Except for in bruteforce.py, which outputs all closest sets of points).

I tried to make this a really elegant program, but should've ended up giving myself a bit more time. While I ended up accomplishing the objectives, the beauty of the code totally fell apart in the end as I started copying and pasting between programs and not doing things the most "pythonic" way. Next time I will allow myself more time and put out better-looking code. Additionally, I would probably visit office hours to debug what was taking so long in my enhanced divide and conquer code.
