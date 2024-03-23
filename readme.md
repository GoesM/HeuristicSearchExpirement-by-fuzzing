# Introduction 

### searching issue
对于一个滑块游戏，即一个方阵，里面有若干个多边形块，

我们给定这个滑块的初始位置和目标位置，要求用搜索算法探索从初始位置到目标位置的方法

### experiment target
我们需要对比在对这一类滑块问题的解决上，传统DFS和启发式搜索的性能区别

### experiment setting

为了更正确地对比算法性能，我们采取模糊测试的方式进行答案探寻

这里我们设计了一个随机滑块游戏生成器,名为 `PuzzleMatrixGenerator` ，可以设定他的长宽高、内部滑块个数等参数，用于生成随机滑块游戏（包括初始状态和目标状态）

然后我们设定了一个自动测试器，名为`fuzzer`，可以针对三种难度（小、大、难）的滑块游戏进行测试

同时在`heuristics.py`文件中提供了一些启发函数的demo，以供测试使用

# usage for demo

展示滑块游戏的随机生成效果：
```sh
python3 puzzle_generator.py
```

测试已有的启发式搜索效果
```sh
python3 fuzzer.py
```
测试过程中，可能会存在无解情况，可以根据需求`Ctrl+C`打断
