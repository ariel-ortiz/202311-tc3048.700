;; Simple examples using webassembly text format

(module

  (func
    (export "meaning_of_life")
    (result i32)

    i32.const 42
  )

  (func
    (export "multiply")
    (param $a i32)
    (param $b i32)
    (result i32)

    local.get $a
    local.get $b
    i32.mul
  )

  (func
    (export "add1")
    (param $x i32)
    (result i32)

    local.get $x
    i32.const 1
    i32.add
  )

  (func
    (export "average")
    (param $x f64)
    (param $y f64)
    (result f64)

    local.get $x
    local.get $y
    f64.add
    f64.const 2
    f64.div
  )
)
