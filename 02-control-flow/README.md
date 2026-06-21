# Control Flow

```bash
python3 02-control-flow/01_if_else.py
```

## Examples

- `01_if_else.py`
- `02_loops.py`
- `03_break_continue_pass.py`
- `04_match_case.py`

→ [03-data-structures](../03-data-structures/)


---

## Interview Preparation

Study **[INTERVIEW_PREP.md](INTERVIEW_PREP.md)** before moving on.

## Next Module

→ [03_Data Structures](../03_data_structures/)


---

## Interview Prep

### Must-Know Concepts

- if/elif/else
- for/while loops
- break/continue/pass
- match/case
- short-circuit evaluation

### Theory Questions

**Q1: Difference between break and continue?**  
A: break exits the loop entirely. continue skips to the next iteration.

**Q2: What does pass do?**  
A: Null operation — placeholder where syntax requires a block but no action is needed.

**Q3: When to use for vs while?**  
A: for: iterate known sequence. while: condition-based, unknown iterations.

**Q4: What is match/case (3.10+)?**  
A: Structural pattern matching — cleaner than long if/elif chains for pattern dispatch.

### Coding Questions

**FizzBuzz**
```python
for i in range(1,101):
    out = 'FizzBuzz' if i%15==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else str(i)
    print(out)
```

**Prime check**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
```

### Common Pitfalls

- Off-by-one errors with range()
- Infinite while loops without update
- break in nested loops only breaks inner loop

