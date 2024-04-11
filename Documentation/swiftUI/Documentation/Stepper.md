Initializer

# init(value:step:label:onEditingChanged:)

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        step: V.Stride = 1,
        @ViewBuilder label: () -> Label,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where V : Strideable

Available when `Label` conforms to `View`.

##  Parameters

`value`

    

The `Binding` to a value that you provide.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s increment or decrement buttons. Defaults to `1`.

`label`

    

A view describing the purpose of this stepper.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a stepper which
causes the execution of the `onEditingChanged` closure at the start and end of
the gesture.

## Discussion

Use this initializer to create a stepper that increments or decrements a bound
value by a specific amount each time the user clicks or taps the stepper’s
increment or decrement buttons.

In the example below, a stepper increments or decrements `value` by the `step`
value of 5 at each click or tap of the control’s increment or decrement
button:

## See Also

### Creating a stepper

`init<F>(value: Binding<F.FormatInput>, step: F.FormatInput.Stride, format: F,
label: () -> Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide, displaying its value with an applied format
style.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, step: V.Stride, onEditingChanged: (Bool) ->
Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, step: F.FormatInput.Stride,
format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, step:
F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

Initializer

# init(value:step:format:label:onEditingChanged:)

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide, displaying its value with an applied format
style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<F>(
        value: Binding<F.FormatInput>,
        step: F.FormatInput.Stride = 1,
        format: F,
        @ViewBuilder label: () -> Label,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String

Available when `Label` conforms to `View`.

##  Parameters

`value`

    

The `Binding` to a value that you provide.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s increment or decrement buttons. Defaults to `1`.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the stepper leaves `value` unchanged. If the user
stops editing the text in an invalid state, the stepper updates the text to
the last known valid value.

`label`

    

A view describing the purpose of this stepper.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a stepper which
causes the execution of the `onEditingChanged` closure at the start and end of
the gesture.

## Discussion

Use this initializer to create a stepper that increments or decrements a bound
value by a specific amount each time the user clicks or taps the stepper’s
increment or decrement buttons, while displaying the current value.

In the example below, a stepper increments or decrements `value` by the `step`
value of 5 at each click or tap of the control’s increment or decrement
button:

## See Also

### Creating a stepper

`init<V>(value: Binding<V>, step: V.Stride, label: () -> Label,
onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, step: V.Stride, onEditingChanged: (Bool) ->
Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, step: F.FormatInput.Stride,
format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, step:
F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

Initializer

# init(_:value:step:onEditingChanged:)

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: Binding<V>,
        step: V.Stride = 1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where V : Strideable

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the stepper’s localized title describing the purpose of the
stepper.

`value`

    

A `Binding` to a value that you provide.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s plus or minus button, respectively. Defaults to `1`.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a `Stepper`
which causes the execution of the `onEditingChanged` closure at the start and
end of the gesture.

## Discussion

Use `Stepper(_:value:step:onEditingChanged:)` to create a stepper with a
custom title that increments or decrements a binding to value by the step size
you specify.

In the example below, the stepper increments or decrements the binding value
by `5` each time the user clicks or taps on the control’s increment or
decrement buttons, respectively:

## See Also

### Creating a stepper

`init<V>(value: Binding<V>, step: V.Stride, label: () -> Label,
onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

Available when `Label` conforms to `View`.

`init<F>(value: Binding<F.FormatInput>, step: F.FormatInput.Stride, format: F,
label: () -> Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide, displaying its value with an applied format
style.

Available when `Label` conforms to `View`.

`init<S, V>(S, value: Binding<V>, step: V.Stride, onEditingChanged: (Bool) ->
Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, step: F.FormatInput.Stride,
format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, step:
F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

Initializer

# init(_:value:step:onEditingChanged:)

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: Binding<V>,
        step: V.Stride = 1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where S : StringProtocol, V : Strideable

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string describing the purpose of the stepper.

`value`

    

The `Binding` to a value that you provide.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s increment or decrement button, respectively. Defaults to `1`.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a `Stepper`
which causes the execution of the `onEditingChanged` closure at the start and
end of the gesture.

## Discussion

Use `Stepper(_:value:step:onEditingChanged:)` to create a stepper with a
custom title that increments or decrements a binding to value by the step size
you specify.

In the example below, the stepper increments or decrements the binding value
by `5` each time one of the user clicks or taps the control’s increment or
decrement buttons:

## See Also

### Creating a stepper

`init<V>(value: Binding<V>, step: V.Stride, label: () -> Label,
onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

Available when `Label` conforms to `View`.

`init<F>(value: Binding<F.FormatInput>, step: F.FormatInput.Stride, format: F,
label: () -> Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide, displaying its value with an applied format
style.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, step: F.FormatInput.Stride,
format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, step:
F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

Initializer

# init(_:value:step:format:onEditingChanged:)

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S, F>(
        _ title: S,
        value: Binding<F.FormatInput>,
        step: F.FormatInput.Stride = 1,
        format: F,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where S : StringProtocol, F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string describing the purpose of the stepper.

`value`

    

The `Binding` to a value that you provide.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s increment or decrement button, respectively. Defaults to `1`.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the stepper leaves `value` unchanged. If the user
stops editing the text in an invalid state, the stepper updates the text to
the last known valid value.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a `Stepper`
which causes the execution of the `onEditingChanged` closure at the start and
end of the gesture.

## Discussion

Use `Stepper(_:value:step:format:onEditingChanged:)` to create a stepper with
a custom title that increments or decrements a binding to value by the step
size you specify, while displaying the current value.

In the example below, the stepper increments or decrements the binding value
by `5` each time one of the user clicks or taps the control’s increment or
decrement buttons:

## See Also

### Creating a stepper

`init<V>(value: Binding<V>, step: V.Stride, label: () -> Label,
onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

Available when `Label` conforms to `View`.

`init<F>(value: Binding<F.FormatInput>, step: F.FormatInput.Stride, format: F,
label: () -> Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide, displaying its value with an applied format
style.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, step: V.Stride, onEditingChanged: (Bool) ->
Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, step:
F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

Initializer

# init(_:value:step:format:onEditingChanged:)

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<F>(
        _ titleKey: LocalizedStringKey,
        value: Binding<F.FormatInput>,
        step: F.FormatInput.Stride = 1,
        format: F,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the stepper’s localized title describing the purpose of the
stepper.

`value`

    

A `Binding` to a value that you provide.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s plus or minus button, respectively. Defaults to `1`.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the stepper leaves `value` unchanged. If the user
stops editing the text in an invalid state, the stepper updates the text to
the last known valid value.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a `Stepper`
which causes the execution of the `onEditingChanged` closure at the start and
end of the gesture.

## Discussion

Use `Stepper(_:value:step:onEditingChanged:)` to create a stepper with a
custom title that increments or decrements a binding to value by the step size
you specify, while displaying the current value.

In the example below, the stepper increments or decrements the binding value
by `5` each time the user clicks or taps on the control’s increment or
decrement buttons, respectively:

## See Also

### Creating a stepper

`init<V>(value: Binding<V>, step: V.Stride, label: () -> Label,
onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

Available when `Label` conforms to `View`.

`init<F>(value: Binding<F.FormatInput>, step: F.FormatInput.Stride, format: F,
label: () -> Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide, displaying its value with an applied format
style.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title key and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, step: V.Stride, onEditingChanged: (Bool) ->
Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, step: F.FormatInput.Stride,
format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper with a title and configured to increment and decrement a
binding to a value and step amount you provide, displaying its value with an
applied format style.

Available when `Label` is `Text`.

Initializer

# init(value:in:step:label:onEditingChanged:)

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V.Stride = 1,
        @ViewBuilder label: () -> Label,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where V : Strideable

Available when `Label` conforms to `View`.

##  Parameters

`value`

    

A `Binding` to a value that you provide.

`bounds`

    

A closed range that describes the upper and lower bounds permitted by the
stepper.

`step`

    

The amount to increment or decrement the stepper when the user clicks or taps
the stepper’s increment or decrement buttons, respectively.

`label`

    

A view describing the purpose of this stepper.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a stepper which
causes the execution of the `onEditingChanged` closure at the start and end of
the gesture.

## Discussion

Use this initializer to create a stepper that increments or decrements a
binding to value by the step size you provide within the given bounds. By
setting the bounds, you ensure that the value never goes below or above the
lowest or highest value, respectively.

The example below shows a stepper that displays the effect of incrementing or
decrementing a value with the step size of `step` with the bounds defined by
`range`:

## See Also

### Creating a stepper over a range

`init<F>(value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>, step:
F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool)
-> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide, displaying its
value with an applied format style.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, in: ClosedRange<V>, step:
V.Stride, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, in:
ClosedRange<F.FormatInput>, step: F.FormatInput.Stride, format: F,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>,
step: F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

Initializer

# init(value:in:step:format:label:onEditingChanged:)

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide, displaying its
value with an applied format style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<F>(
        value: Binding<F.FormatInput>,
        in bounds: ClosedRange<F.FormatInput>,
        step: F.FormatInput.Stride = 1,
        format: F,
        @ViewBuilder label: () -> Label,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String

Available when `Label` conforms to `View`.

##  Parameters

`value`

    

A `Binding` to a value that you provide.

`bounds`

    

A closed range that describes the upper and lower bounds permitted by the
stepper.

`step`

    

The amount to increment or decrement the stepper when the user clicks or taps
the stepper’s increment or decrement buttons, respectively.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the stepper leaves `value` unchanged. If the user
stops editing the text in an invalid state, the stepper updates the text to
the last known valid value.

`label`

    

A view describing the purpose of this stepper.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a stepper which
causes the execution of the `onEditingChanged` closure at the start and end of
the gesture.

## Discussion

Use this initializer to create a stepper that increments or decrements a
binding to value by the step size you provide within the given bounds. By
setting the bounds, you ensure that the value never goes below or above the
lowest or highest value, respectively.

The example below shows a stepper that displays the effect of incrementing or
decrementing a value with the step size of `step` with the bounds defined by
`range`:

## See Also

### Creating a stepper over a range

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, in: ClosedRange<V>, step:
V.Stride, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, in:
ClosedRange<F.FormatInput>, step: F.FormatInput.Stride, format: F,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>,
step: F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

Initializer

# init(_:value:in:step:onEditingChanged:)

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V.Stride = 1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where V : Strideable

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the stepper’s localized title describing the purpose of the
stepper.

`value`

    

A `Binding` to a value that your provide.

`bounds`

    

A closed range that describes the upper and lower bounds permitted by the
stepper.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s increment or decrement button, respectively. Defaults to `1`.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a `Stepper`
which causes the execution of the `onEditingChanged` closure at the start and
end of the gesture.

## Discussion

Use `Stepper(_:value:in:step:onEditingChanged:)` to create a stepper that
increments or decrements a value within a specific range of values by a
specific step size. In the example below, a stepper increments or decrements a
binding to value over a range of `1...50` by `5` at each press of the
stepper’s increment or decrement buttons:

## See Also

### Creating a stepper over a range

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

Available when `Label` conforms to `View`.

`init<F>(value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>, step:
F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool)
-> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide, displaying its
value with an applied format style.

Available when `Label` conforms to `View`.

`init<S, V>(S, value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, in:
ClosedRange<F.FormatInput>, step: F.FormatInput.Stride, format: F,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>,
step: F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

Initializer

# init(_:value:in:step:onEditingChanged:)

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V.Stride = 1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where S : StringProtocol, V : Strideable

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string describing the purpose of the stepper.

`value`

    

A `Binding` to a value that your provide.

`bounds`

    

A closed range that describes the upper and lower bounds permitted by the
stepper.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s increment or decrement button, respectively. Defaults to `1`.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a `Stepper`
which causes the execution of the `onEditingChanged` closure at the start and
end of the gesture.

## Discussion

Use `Stepper(_:value:in:step:onEditingChanged:)` to create a stepper that
increments or decrements a value within a specific range of values by a
specific step size. In the example below, a stepper increments or decrements a
binding to value over a range of `1...50` by `5` each time the user clicks or
taps the stepper’s increment or decrement buttons:

## See Also

### Creating a stepper over a range

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

Available when `Label` conforms to `View`.

`init<F>(value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>, step:
F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool)
-> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide, displaying its
value with an applied format style.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, in: ClosedRange<V>, step:
V.Stride, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, in:
ClosedRange<F.FormatInput>, step: F.FormatInput.Stride, format: F,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>,
step: F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

Initializer

# init(_:value:in:step:format:onEditingChanged:)

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<F>(
        _ titleKey: LocalizedStringKey,
        value: Binding<F.FormatInput>,
        in bounds: ClosedRange<F.FormatInput>,
        step: F.FormatInput.Stride = 1,
        format: F,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the stepper’s localized title describing the purpose of the
stepper.

`value`

    

A `Binding` to a value that your provide.

`bounds`

    

A closed range that describes the upper and lower bounds permitted by the
stepper.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s increment or decrement button, respectively. Defaults to `1`.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the stepper leaves `value` unchanged. If the user
stops editing the text in an invalid state, the stepper updates the text to
the last known valid value.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a `Stepper`
which causes the execution of the `onEditingChanged` closure at the start and
end of the gesture.

## Discussion

Use `Stepper(_:value:in:step:format:onEditingChanged:)` to create a stepper
that increments or decrements a value within a specific range of values by a
specific step size, while displaying the current value. In the example below,
a stepper increments or decrements a binding to value over a range of `1...50`
by `5` each time the user clicks or taps the stepper’s increment or decrement
buttons:

## See Also

### Creating a stepper over a range

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

Available when `Label` conforms to `View`.

`init<F>(value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>, step:
F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool)
-> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide, displaying its
value with an applied format style.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, in: ClosedRange<V>, step:
V.Stride, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<S, F>(S, value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>,
step: F.FormatInput.Stride, format: F, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

Initializer

# init(_:value:in:step:format:onEditingChanged:)

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S, F>(
        _ title: S,
        value: Binding<F.FormatInput>,
        in bounds: ClosedRange<F.FormatInput>,
        step: F.FormatInput.Stride = 1,
        format: F,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where S : StringProtocol, F : ParseableFormatStyle, F.FormatInput : BinaryFloatingPoint, F.FormatOutput == String

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string describing the purpose of the stepper.

`value`

    

A `Binding` to a value that your provide.

`bounds`

    

A closed range that describes the upper and lower bounds permitted by the
stepper.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s increment or decrement button, respectively. Defaults to `1`.

`format`

    

A format style of type `F` to use when converting between the string the user
edits and the underlying value of type `F.FormatInput`. If `format` can’t
perform the conversion, the stepper leaves `value` unchanged. If the user
stops editing the text in an invalid state, the stepper updates the text to
the last known valid value.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a `Stepper`
which causes the execution of the `onEditingChanged` closure at the start and
end of the gesture.

## Discussion

Use `Stepper(_:value:in:step:format:onEditingChanged:)` to create a stepper
that increments or decrements a value within a specific range of values by a
specific step size, while displaying the current value. In the example below,
a stepper increments or decrements a binding to value over a range of `1...50`
by `5` each time the user clicks or taps the stepper’s increment or decrement
buttons:

## See Also

### Creating a stepper over a range

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, onEditingChanged: (Bool) -> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

Available when `Label` conforms to `View`.

`init<F>(value: Binding<F.FormatInput>, in: ClosedRange<F.FormatInput>, step:
F.FormatInput.Stride, format: F, label: () -> Label, onEditingChanged: (Bool)
-> Void)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide, displaying its
value with an applied format style.

Available when `Label` conforms to `View`.

`init<V>(LocalizedStringKey, value: Binding<V>, in: ClosedRange<V>, step:
V.Stride, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<S, V>(S, value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide.

Available when `Label` is `Text`.

`init<F>(LocalizedStringKey, value: Binding<F.FormatInput>, in:
ClosedRange<F.FormatInput>, step: F.FormatInput.Stride, format: F,
onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that increments and decrements a binding to a
value, by a step size and within a closed range that you provide, displaying
its value with an applied format style.

Available when `Label` is `Text`.

Initializer

# init(label:onIncrement:onDecrement:onEditingChanged:)

Creates a stepper instance that performs the closures you provide when the
user increments or decrements the stepper.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        @ViewBuilder label: () -> Label,
        onIncrement: (() -> Void)?,
        onDecrement: (() -> Void)?,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    )

##  Parameters

`label`

    

A view describing the purpose of this stepper.

`onIncrement`

    

The closure to execute when the user clicks or taps the control’s plus button.

`onDecrement`

    

The closure to execute when the user clicks or taps the control’s minus
button.

`onEditingChanged`

    

A closure called when editing begins and ends. For example, on iOS, the user
may touch and hold the increment or decrement buttons on a `Stepper` which
causes the execution of the `onEditingChanged` closure at the start and end of
the gesture.

## Discussion

Use this initializer to create a control with a custom title that executes
closures you provide when the user clicks or taps the stepper’s increment or
decrement buttons.

The example below uses an array that holds a number of `Color` values, a local
state variable, `value`, to set the control’s background color, and title
label. When the user clicks or taps on the stepper’s increment or decrement
buttons SwiftUI executes the relevant closure that updates `value`, wrapping
the `value` to prevent overflow. SwiftUI then re-renders the view, updating
the text and background color to match the current index:

}

## See Also

### Creating a stepper with change behavior

`init(LocalizedStringKey, onIncrement: (() -> Void)?, onDecrement: (() ->
Void)?, onEditingChanged: (Bool) -> Void)`

Creates a stepper that uses a title key and executes the closures you provide
when the user clicks or taps the stepper’s increment and decrement buttons.

Available when `Label` is `Text`.

`init<S>(S, onIncrement: (() -> Void)?, onDecrement: (() -> Void)?,
onEditingChanged: (Bool) -> Void)`

Creates a stepper using a title string and that executes closures you provide
when the user clicks or taps the stepper’s increment or decrement buttons.

Available when `Label` is `Text`.

Initializer

# init(_:onIncrement:onDecrement:onEditingChanged:)

Creates a stepper that uses a title key and executes the closures you provide
when the user clicks or taps the stepper’s increment and decrement buttons.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        onIncrement: (() -> Void)?,
        onDecrement: (() -> Void)?,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the stepper’s localized title describing the purpose of the
stepper.

`onIncrement`

    

The closure to execute when the user clicks or taps the control’s plus button.

`onDecrement`

    

The closure to execute when the user clicks or taps the control’s minus
button.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a `Stepper`
which causes the execution of the `onEditingChanged` closure at the start and
end of the gesture.

## Discussion

Use this initializer to create a stepper with a custom title that executes
closures you provide when either of the stepper’s increment or decrement
buttons are pressed. This version of `Stepper` doesn’t take a binding to a
value, nor does it allow you to specify a range of acceptable values, or a
step value – it simply calls the closures you provide when the control’s
buttons are pressed.

The example below uses an array that holds a number of `Color` values, a local
state variable, `value`, to set the control’s background color, and title
label. When the user clicks or taps on the stepper’s increment or decrement
buttons SwiftUI executes the relevant closure that updates `value`, wrapping
the `value` to prevent overflow. SwiftUI then re-renders the view, updating
the text and background color to match the current index:

## See Also

### Creating a stepper with change behavior

`init(label: () -> Label, onIncrement: (() -> Void)?, onDecrement: (() ->
Void)?, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that performs the closures you provide when the
user increments or decrements the stepper.

`init<S>(S, onIncrement: (() -> Void)?, onDecrement: (() -> Void)?,
onEditingChanged: (Bool) -> Void)`

Creates a stepper using a title string and that executes closures you provide
when the user clicks or taps the stepper’s increment or decrement buttons.

Available when `Label` is `Text`.

Initializer

# init(_:onIncrement:onDecrement:onEditingChanged:)

Creates a stepper using a title string and that executes closures you provide
when the user clicks or taps the stepper’s increment or decrement buttons.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        onIncrement: (() -> Void)?,
        onDecrement: (() -> Void)?,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

A string describing the purpose of the stepper.

`onIncrement`

    

The closure to execute when the user clicks or taps the control’s plus button.

`onDecrement`

    

The closure to execute when the user clicks or taps the control’s minus
button.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a `Stepper`
which causes the execution of the `onEditingChanged` closure at the start and
end of the gesture.

## Discussion

Use `Stepper(_:onIncrement:onDecrement:onEditingChanged:)` to create a control
with a custom title that executes closures you provide when the user clicks or
taps on the stepper’s increment or decrement buttons.

The example below uses an array that holds a number of `Color` values, a local
state variable, `value`, to set the control’s background color, and title
label. When the user clicks or taps on the stepper’s increment or decrement
buttons SwiftUI executes the relevant closure that updates `value`, wrapping
the `value` to prevent overflow. SwiftUI then re-renders the view, updating
the text and background color to match the current index:

## See Also

### Creating a stepper with change behavior

`init(label: () -> Label, onIncrement: (() -> Void)?, onDecrement: (() ->
Void)?, onEditingChanged: (Bool) -> Void)`

Creates a stepper instance that performs the closures you provide when the
user increments or decrements the stepper.

`init(LocalizedStringKey, onIncrement: (() -> Void)?, onDecrement: (() ->
Void)?, onEditingChanged: (Bool) -> Void)`

Creates a stepper that uses a title key and executes the closures you provide
when the user clicks or taps the stepper’s increment and decrement buttons.

Available when `Label` is `Text`.

Initializer

# init(value:step:onEditingChanged:label:)

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 9.0–10.4  Deprecated
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        step: V.Stride = 1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in },
        @ViewBuilder label: () -> Label
    ) where V : Strideable

Available when `Label` conforms to `View`.

Deprecated

Use `init(value:step:label:onEditingChanged:)` instead.

##  Parameters

`value`

    

The `Binding` to a value that you provide.

`step`

    

The amount to increment or decrement `value` each time the user clicks or taps
the stepper’s increment or decrement buttons. Defaults to `1`.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a stepper which
causes the execution of the `onEditingChanged` closure at the start and end of
the gesture.

`label`

    

A view describing the purpose of this stepper.

## Discussion

Use this initializer to create a stepper that increments or decrements a bound
value by a specific amount each time the user clicks or taps the stepper’s
increment or decrement buttons.

In the example below, a stepper increments or decrements `value` by the `step`
value of 5 at each click or tap of the control’s increment or decrement
button:

## See Also

### Deprecated initializers

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, label: () -> Label)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

Available when `Label` conforms to `View`.

Deprecated

`init(onIncrement: (() -> Void)?, onDecrement: (() -> Void)?,
onEditingChanged: (Bool) -> Void, label: () -> Label)`

Creates a stepper instance that performs the closures you provide when the
user increments or decrements the stepper.

Available when `Label` conforms to `View`.

Deprecated

Initializer

# init(value:in:step:onEditingChanged:label:)

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 9.0–10.4  Deprecated
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V.Stride = 1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in },
        @ViewBuilder label: () -> Label
    ) where V : Strideable

Available when `Label` conforms to `View`.

Deprecated

Use `init(value:in:step:label:onEditingChanged:)` instead.

##  Parameters

`value`

    

A `Binding` to a value that you provide.

`bounds`

    

A closed range that describes the upper and lower bounds permitted by the
stepper.

`step`

    

The amount to increment or decrement the stepper when the user clicks or taps
the stepper’s increment or decrement buttons, respectively.

`onEditingChanged`

    

A closure that’s called when editing begins and ends. For example, on iOS, the
user may touch and hold the increment or decrement buttons on a stepper which
causes the execution of the `onEditingChanged` closure at the start and end of
the gesture.

`label`

    

A view describing the purpose of this stepper.

## Discussion

Use this initializer to create a stepper that increments or decrements a
binding to value by the step size you provide within the given bounds. By
setting the bounds, you ensure that the value never goes below or above the
lowest or highest value, respectively.

The example below shows a stepper that displays the effect of incrementing or
decrementing a value with the step size of `step` with the bounds defined by
`range`:

## See Also

### Deprecated initializers

`init<V>(value: Binding<V>, step: V.Stride, onEditingChanged: (Bool) -> Void,
label: () -> Label)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

Available when `Label` conforms to `View`.

Deprecated

`init(onIncrement: (() -> Void)?, onDecrement: (() -> Void)?,
onEditingChanged: (Bool) -> Void, label: () -> Label)`

Creates a stepper instance that performs the closures you provide when the
user increments or decrements the stepper.

Available when `Label` conforms to `View`.

Deprecated

Initializer

# init(onIncrement:onDecrement:onEditingChanged:label:)

Creates a stepper instance that performs the closures you provide when the
user increments or decrements the stepper.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 9.0–10.4  Deprecated
visionOS 1.0+

    
    
    init(
        onIncrement: (() -> Void)?,
        onDecrement: (() -> Void)?,
        onEditingChanged: @escaping (Bool) -> Void = { _ in },
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

Deprecated

Use `init(label:onIncrement:onDecrement:onEditingChanged:)` instead.

##  Parameters

`onIncrement`

    

The closure to execute when the user clicks or taps the control’s plus button.

`onDecrement`

    

The closure to execute when the user clicks or taps the control’s minus
button.

`onEditingChanged`

    

A closure called when editing begins and ends. For example, on iOS, the user
may touch and hold the increment or decrement buttons on a `Stepper` which
causes the execution of the `onEditingChanged` closure at the start and end of
the gesture.

`label`

    

A view describing the purpose of this stepper.

## Discussion

Use this initializer to create a control with a custom title that executes
closures you provide when the user clicks or taps the stepper’s increment or
decrement buttons.

The example below uses an array that holds a number of `Color` values, a local
state variable, `value`, to set the control’s background color, and title
label. When the user clicks or taps on the stepper’s increment or decrement
buttons SwiftUI executes the relevant closure that updates `value`, wrapping
the `value` to prevent overflow. SwiftUI then re-renders the view, updating
the text and background color to match the current index:

}

## See Also

### Deprecated initializers

`init<V>(value: Binding<V>, step: V.Stride, onEditingChanged: (Bool) -> Void,
label: () -> Label)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value you provide.

Available when `Label` conforms to `View`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, label: () -> Label)`

Creates a stepper configured to increment or decrement a binding to a value
using a step value and within a range of values you provide.

Available when `Label` conforms to `View`.

Deprecated

