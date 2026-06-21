# Concurrency

```bash
python3 16-concurrency/01_threading.py
```

## Examples

- `01_threading.py`
- `02_multiprocessing.py`
- `03_asyncio.py`

→ [17-advanced](../17-advanced/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [17_Advanced Python Internals](../17_advanced_python_internals/)


---

## Interview Prep

### Must-Know Concepts

- threading
- multiprocessing
- asyncio
- GIL
- Lock
- Queue

### Theory Questions

**Q1: Thread vs Process?**  
A: Thread: shared memory, GIL limited. Process: separate memory, true CPU parallelism.

**Q2: When asyncio?**  
A: High concurrency I/O — websockets, API calls.

**Q3: What is GIL?**  
A: One thread executes bytecode at a time.

### Coding Questions


### Common Pitfalls

- Race conditions without Lock
- Using threads for CPU-bound work

