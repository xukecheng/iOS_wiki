Initializer

# init(value:in:onEditingChanged:)

Creates a slider to select a value from a given range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V> = 0...1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint

Available when `Label` is `EmptyView` and `ValueLabel` is `EmptyView`.

##  Parameters

`value`

    

The selected value within `bounds`.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`onEditingChanged`

    

A callback for when editing begins and ends.

## Discussion

The `value` of the created instance is equal to the position of the given
value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example,
on iOS, editing begins when the user starts to drag the thumb along the
slider’s track.

## See Also

### Creating a slider

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, subject to a step
increment.

Available when `Label` is `EmptyView` and `ValueLabel` is `EmptyView`.

Initializer

# init(value:in:step:onEditingChanged:)

Creates a slider to select a value from a given range, subject to a step
increment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V.Stride = 1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint

Available when `Label` is `EmptyView` and `ValueLabel` is `EmptyView`.

##  Parameters

`value`

    

The selected value within `bounds`.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`step`

    

The distance between each valid value.

`onEditingChanged`

    

A callback for when editing begins and ends.

## Discussion

The `value` of the created instance is equal to the position of the given
value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example,
on iOS, editing begins when the user starts to drag the thumb along the
slider’s track.

## See Also

### Creating a slider

`init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) ->
Void)`

Creates a slider to select a value from a given range.

Available when `Label` is `EmptyView` and `ValueLabel` is `EmptyView`.

Initializer

# init(value:in:label:onEditingChanged:)

Creates a slider to select a value from a given range, which displays the
provided label.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

##  Parameters

`value`

    

The selected value within `bounds`.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A `View` that describes the purpose of the instance. Not all slider styles
show the label, but even in those cases, SwiftUI uses the label for
accessibility. For example, VoiceOver uses the label to identify the purpose
of the slider.

`onEditingChanged`

    

A callback for when editing begins and ends.

## Discussion

The `value` of the created instance is equal to the position of the given
value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example,
on iOS, editing begins when the user starts to drag the thumb along the
slider’s track.

## See Also

### Creating a slider with labels

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label,
minimumValueLabel: () -> ValueLabel, maximumValueLabel: () -> ValueLabel,
onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, which displays the
provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, minimumValueLabel: () -> ValueLabel, maximumValueLabel: () ->
ValueLabel, onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Initializer

# init(value:in:step:label:onEditingChanged:)

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided label.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V.Stride = 1,
        @ViewBuilder label: () -> Label,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

##  Parameters

`value`

    

The selected value within `bounds`.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`step`

    

The distance between each valid value.

`label`

    

A `View` that describes the purpose of the instance. Not all slider styles
show the label, but even in those cases, SwiftUI uses the label for
accessibility. For example, VoiceOver uses the label to identify the purpose
of the slider.

`onEditingChanged`

    

A callback for when editing begins and ends.

## Discussion

The `value` of the created instance is equal to the position of the given
value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example,
on iOS, editing begins when the user starts to drag the thumb along the
slider’s track.

## See Also

### Creating a slider with labels

`init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label,
onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, which displays the
provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label,
minimumValueLabel: () -> ValueLabel, maximumValueLabel: () -> ValueLabel,
onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, which displays the
provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, minimumValueLabel: () -> ValueLabel, maximumValueLabel: () ->
ValueLabel, onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Initializer

# init(value:in:label:minimumValueLabel:maximumValueLabel:onEditingChanged:)

Creates a slider to select a value from a given range, which displays the
provided labels.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V> = 0...1,
        @ViewBuilder label: () -> Label,
        @ViewBuilder minimumValueLabel: () -> ValueLabel,
        @ViewBuilder maximumValueLabel: () -> ValueLabel,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

##  Parameters

`value`

    

The selected value within `bounds`.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`label`

    

A `View` that describes the purpose of the instance. Not all slider styles
show the label, but even in those cases, SwiftUI uses the label for
accessibility. For example, VoiceOver uses the label to identify the purpose
of the slider.

`minimumValueLabel`

    

A view that describes `bounds.lowerBound`.

`maximumValueLabel`

    

A view that describes `bounds.lowerBound`.

`onEditingChanged`

    

A callback for when editing begins and ends.

## Discussion

The `value` of the created instance is equal to the position of the given
value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example,
on iOS, editing begins when the user starts to drag the thumb along the
slider’s track.

## See Also

### Creating a slider with labels

`init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label,
onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, which displays the
provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, minimumValueLabel: () -> ValueLabel, maximumValueLabel: () ->
ValueLabel, onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Initializer

#
init(value:in:step:label:minimumValueLabel:maximumValueLabel:onEditingChanged:)

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided labels.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V.Stride = 1,
        @ViewBuilder label: () -> Label,
        @ViewBuilder minimumValueLabel: () -> ValueLabel,
        @ViewBuilder maximumValueLabel: () -> ValueLabel,
        onEditingChanged: @escaping (Bool) -> Void = { _ in }
    ) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

##  Parameters

`value`

    

The selected value within `bounds`.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`step`

    

The distance between each valid value.

`label`

    

A `View` that describes the purpose of the instance. Not all slider styles
show the label, but even in those cases, SwiftUI uses the label for
accessibility. For example, VoiceOver uses the label to identify the purpose
of the slider.

`minimumValueLabel`

    

A view that describes `bounds.lowerBound`.

`maximumValueLabel`

    

A view that describes `bounds.lowerBound`.

`onEditingChanged`

    

A callback for when editing begins and ends.

## Discussion

The `value` of the created instance is equal to the position of the given
value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example,
on iOS, editing begins when the user starts to drag the thumb along the
slider’s track.

## See Also

### Creating a slider with labels

`init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label,
onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, which displays the
provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () ->
Label, onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

`init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label,
minimumValueLabel: () -> ValueLabel, maximumValueLabel: () -> ValueLabel,
onEditingChanged: (Bool) -> Void)`

Creates a slider to select a value from a given range, which displays the
provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Initializer

# init(value:in:onEditingChanged:label:)

Creates a slider to select a value from a given range, which displays the
provided label.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 6.0–10.4  Deprecated
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V> = 0...1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in },
        @ViewBuilder label: () -> Label
    ) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

Deprecated

Use `init(value:in:label:onEditingChanged:)` instead.

##  Parameters

`value`

    

The selected value within `bounds`.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`onEditingChanged`

    

A callback for when editing begins and ends.

`label`

    

A `View` that describes the purpose of the instance. Not all slider styles
show the label, but even in those cases, SwiftUI uses the label for
accessibility. For example, VoiceOver uses the label to identify the purpose
of the slider.

## Discussion

The `value` of the created instance is equal to the position of the given
value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example,
on iOS, editing begins when the user starts to drag the thumb along the
slider’s track.

## See Also

### Deprecated initializers

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, label: () -> Label)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) ->
Void, minimumValueLabel: ValueLabel, maximumValueLabel: ValueLabel, label: ()
-> Label)`

Creates a slider to select a value from a given range, which displays the
provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, minimumValueLabel: ValueLabel,
maximumValueLabel: ValueLabel, label: () -> Label)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Deprecated

Initializer

# init(value:in:step:onEditingChanged:label:)

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided label.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 6.0–10.4  Deprecated
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V.Stride = 1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in },
        @ViewBuilder label: () -> Label
    ) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

Deprecated

Use `init(value:in:step:label:onEditingChanged:)` instead.

##  Parameters

`value`

    

The selected value within `bounds`.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`step`

    

The distance between each valid value.

`onEditingChanged`

    

A callback for when editing begins and ends.

`label`

    

A `View` that describes the purpose of the instance. Not all slider styles
show the label, but even in those cases, SwiftUI uses the label for
accessibility. For example, VoiceOver uses the label to identify the purpose
of the slider.

## Discussion

The `value` of the created instance is equal to the position of the given
value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example,
on iOS, editing begins when the user starts to drag the thumb along the
slider’s track.

## See Also

### Deprecated initializers

`init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) ->
Void, label: () -> Label)`

Creates a slider to select a value from a given range, which displays the
provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) ->
Void, minimumValueLabel: ValueLabel, maximumValueLabel: ValueLabel, label: ()
-> Label)`

Creates a slider to select a value from a given range, which displays the
provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, minimumValueLabel: ValueLabel,
maximumValueLabel: ValueLabel, label: () -> Label)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Deprecated

Initializer

# init(value:in:onEditingChanged:minimumValueLabel:maximumValueLabel:label:)

Creates a slider to select a value from a given range, which displays the
provided labels.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 6.0–10.4  Deprecated
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V> = 0...1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in },
        minimumValueLabel: ValueLabel,
        maximumValueLabel: ValueLabel,
        @ViewBuilder label: () -> Label
    ) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Deprecated

Use
`init(value:in:label:minimumValueLabel:maximumValueLabel:onEditingChanged:)`
instead.

##  Parameters

`value`

    

The selected value within `bounds`.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`onEditingChanged`

    

A callback for when editing begins and ends.

`minimumValueLabel`

    

A view that describes `bounds.lowerBound`.

`maximumValueLabel`

    

A view that describes `bounds.lowerBound`.

`label`

    

A `View` that describes the purpose of the instance. Not all slider styles
show the label, but even in those cases, SwiftUI uses the label for
accessibility. For example, VoiceOver uses the label to identify the purpose
of the slider.

## Discussion

The `value` of the created instance is equal to the position of the given
value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example,
on iOS, editing begins when the user starts to drag the thumb along the
slider’s track.

## See Also

### Deprecated initializers

`init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) ->
Void, label: () -> Label)`

Creates a slider to select a value from a given range, which displays the
provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, label: () -> Label)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, minimumValueLabel: ValueLabel,
maximumValueLabel: ValueLabel, label: () -> Label)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Deprecated

Initializer

#
init(value:in:step:onEditingChanged:minimumValueLabel:maximumValueLabel:label:)

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided labels.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  watchOS 6.0–10.4  Deprecated
visionOS 1.0+

    
    
    init<V>(
        value: Binding<V>,
        in bounds: ClosedRange<V>,
        step: V.Stride = 1,
        onEditingChanged: @escaping (Bool) -> Void = { _ in },
        minimumValueLabel: ValueLabel,
        maximumValueLabel: ValueLabel,
        @ViewBuilder label: () -> Label
    ) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Deprecated

Use
`init(value:in:step:label:minimumValueLabel:maximumValueLabel:onEditingChanged:)`
instead.

##  Parameters

`value`

    

The selected value within `bounds`.

`bounds`

    

The range of the valid values. Defaults to `0...1`.

`step`

    

The distance between each valid value.

`onEditingChanged`

    

A callback for when editing begins and ends.

`minimumValueLabel`

    

A view that describes `bounds.lowerBound`.

`maximumValueLabel`

    

A view that describes `bounds.lowerBound`.

`label`

    

A `View` that describes the purpose of the instance. Not all slider styles
show the label, but even in those cases, SwiftUI uses the label for
accessibility. For example, VoiceOver uses the label to identify the purpose
of the slider.

## Discussion

The `value` of the created instance is equal to the position of the given
value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example,
on iOS, editing begins when the user starts to drag the thumb along the
slider’s track.

## See Also

### Deprecated initializers

`init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) ->
Void, label: () -> Label)`

Creates a slider to select a value from a given range, which displays the
provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride,
onEditingChanged: (Bool) -> Void, label: () -> Label)`

Creates a slider to select a value from a given range, subject to a step
increment, which displays the provided label.

Available when `Label` conforms to `View` and `ValueLabel` is `EmptyView`.

Deprecated

`init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) ->
Void, minimumValueLabel: ValueLabel, maximumValueLabel: ValueLabel, label: ()
-> Label)`

Creates a slider to select a value from a given range, which displays the
provided labels.

Available when `Label` conforms to `View` and `ValueLabel` conforms to `View`.

Deprecated

