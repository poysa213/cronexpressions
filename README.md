
# CronExpressions

A Python library that simplifies the creation and management of cron expressions. **CronExpressions** provides an intuitive, readable approach to writing cron syntax, making it easier to generate complex scheduling patterns without struggling with traditional cron expression notation.

## Features

- **Simplified Cron Expression Writing**: Easily create complex cron expressions using a fluent, chainable API.
- **Readable Syntax**: Transform cryptic cron strings into clear, understandable code.
- **Flexible Expression Building**: Construct cron expressions with an intuitive, step-by-step approach.

## Installation

Install the package using pip:

```bash
pip install cronexpressions
```

## Usage Guide

### Predefined Constants

The library provides some predefined cron expression constants for quick reference:

```python
from cronexpressions import CronExpression
print(CronExpression.EVERY_MINUTE)  # Outputs a standard cron expression for every minute
print(CronExpression.EVERY_HOUR)    # Outputs a standard cron expression for every hour
print(CronExpression.EVERY_DAY)     # Outputs a standard cron expression for daily execution
```

### Building Cron Expressions

Use the `CronBuilder` class to construct cron expressions with ease:

#### Create Basic Expressions

```python
from cronexpressions import CronBuilder
# Build a cron expression to run at 10:30:15 every day
cron = CronBuilder().set_second("15").set_minute("30").set_hour("10").build()
print(cron)  # Outputs a cron expression representing this specific time
```

#### Recurring Intervals

```python
# Create an expression to run every 5 minutes
cron = CronBuilder().every('minute', 5).build()
print(cron)  # Outputs a cron expression for every 5 minutes

# Create an expression to run every 2 hours
cron = CronBuilder().every('hour', 2).build()
print(cron)  # Outputs a cron expression for every 2 hours
```

#### Range-based Expressions

```python
# Create an expression for hours between 9 AM and 5 PM
cron = CronBuilder().set_range('hour', 9, 17).build()
print(cron)  # Outputs a cron expression covering this hour range
```

#### Specific Occurrences

```python
# Create an expression for the first Monday of each month
cron = CronBuilder().set_specific('weekday', '1#1').build()
print(cron)  # Outputs a cron expression for this specific occurrence
```

## Important Note

**CronExpressions** is a utility library for generating cron expressions. It does not handle job scheduling itself - it simply helps you create readable and maintainable cron syntax.

## Use Cases

- Generating cron expressions for scheduling libraries
- Making cron syntax more readable and maintainable
- Simplifying complex scheduling patterns
- Providing a more intuitive interface for working with cron expressions

## Inspiration

This library was inspired by two key motivations:

1. The [NestJS Schedule Module](https://github.com/nestjs/schedule/), which provides an elegant way to manage cron expressions in Node.js.

2. The common struggles developers face when working with traditional, cryptic cron syntax. Developers often find themselves:
   - Spending excessive time deciphering complex cron expressions
   - Making errors due to the unintuitive nature of standard cron notation
   - Requiring constant reference to cron syntax guides
   - Struggling to quickly understand or modify existing cron schedules

**CronExpressions** aims to address these challenges by bringing a more intuitive, readable approach to cron expression generation in the Python ecosystem.

Contributions and feedback are welcome! 🚀