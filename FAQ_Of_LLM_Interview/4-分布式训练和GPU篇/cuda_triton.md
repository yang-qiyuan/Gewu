# Cuda, Kernel, and Triton

## Benchmarking and Profiling Performance Essentials
### Bench Marking: How long does it take?
1. A part for warm-up: first times might be slower due to compilation, things not cached.
2. A part for cuda synchronization
3. A part for core code
4. Average the performance and return the result

### Profiling: Which part takes most time?
