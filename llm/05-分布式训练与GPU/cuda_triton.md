# Cuda, Kernel, and Triton

## Benchmarking and Profiling Performance Essentials
### Bench Marking: How long does it take?
1. A part for warm-up: first times might be slower due to compilation, things not cached.
2. A part for cuda synchronization
3. A part for core code
4. Average the performance and return the result

### Profiling: Which part takes most time?

<!-- related:start -->
## 相关笔记

- [分布式训练与GPU索引](%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%AD%E7%BB%83%E4%B8%8EGPU%E7%B4%A2%E5%BC%95.md)
- [large_scale_training](large_scale_training.md)
<!-- related:end -->
