# Performance

```bash
python3 18-performance/01_gil_and_threading_impact.py
```

## Examples

- `01_gil_and_threading_impact.py`
- `02_memory_and_references.py`
- `03_profiling_timeit.py`
- `04_optimization_patterns.py`

→ [19-best-practices](../19-best-practices/)


---

## Interview Prep

### Must-Know Concepts

- GIL
- ref counting
- gc
- cProfile
- timeit
- slots

### Theory Questions

**Q1: How Python manages memory?**  
A: Reference counting + cyclic garbage collector.

**Q2: Profile before optimize?**  
A: Always. Fix algorithm first.

### Coding Questions


### Common Pitfalls

- Optimizing without measuring
- Unnecessary copies of large data

