Initializer

# init()

Creates a progress view for showing indeterminate progress, without a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init() where Label == EmptyView

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

## See Also

### Creating an indeterminate progress view

`init(label: () -> Label)`

Creates a progress view for showing indeterminate progress that displays a
custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(LocalizedStringKey)`

Creates a progress view for showing indeterminate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init<S>(S)`

Creates a progress view for showing indeterminate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

Initializer

# init(label:)

Creates a progress view for showing indeterminate progress that displays a
custom label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(@ViewBuilder label: () -> Label)

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

##  Parameters

`label`

    

A view builder that creates a view that describes the task in progress.

## See Also

### Creating an indeterminate progress view

`init()`

Creates a progress view for showing indeterminate progress, without a label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(LocalizedStringKey)`

Creates a progress view for showing indeterminate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init<S>(S)`

Creates a progress view for showing indeterminate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

Initializer

# init(_:)

Creates a progress view for showing indeterminate progress that generates its
label from a localized string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ titleKey: LocalizedStringKey) where Label == Text

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

##  Parameters

`titleKey`

    

The key for the progress view’s localized title that describes the task in
progress.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings. To initialize a indeterminate
progress view with a string variable, use the corresponding initializer that
takes a `StringProtocol` instance.

## See Also

### Creating an indeterminate progress view

`init()`

Creates a progress view for showing indeterminate progress, without a label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(label: () -> Label)`

Creates a progress view for showing indeterminate progress that displays a
custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init<S>(S)`

Creates a progress view for showing indeterminate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

Initializer

# init(_:)

Creates a progress view for showing indeterminate progress that generates its
label from a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(_ title: S) where Label == Text, S : StringProtocol

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

##  Parameters

`title`

    

A string that describes the task in progress.

## Discussion

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(verbatim:)`. See `Text` for more information about localizing
strings. To initialize a progress view with a localized string key, use the
corresponding initializer that takes a `LocalizedStringKey` instance.

## See Also

### Creating an indeterminate progress view

`init()`

Creates a progress view for showing indeterminate progress, without a label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(label: () -> Label)`

Creates a progress view for showing indeterminate progress that displays a
custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

`init(LocalizedStringKey)`

Creates a progress view for showing indeterminate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`EmptyView`.

Initializer

# init(_:)

Creates a progress view for visualizing the given progress instance.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ progress: Progress) where Label == EmptyView, CurrentValueLabel == EmptyView

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

## Discussion

The progress view synthesizes a default label using the `localizedDescription`
of the given progress instance.

## See Also

### Creating a determinate progress view

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(value:total:)

Creates a progress view for showing determinate progress.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<V>(
        value: V?,
        total: V = 1.0
    ) where Label == EmptyView, CurrentValueLabel == EmptyView, V : BinaryFloatingPoint

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`value`

    

The completed amount of the task to this point, in a range of `0.0` to
`total`, or `nil` if the progress is indeterminate.

`total`

    

The full amount representing the complete scope of the task, meaning the task
is complete if `value` equals `total`. The default value is `1.0`.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the
progress view pins the value to those limits, rounding to the nearest possible
bound. A value of `nil` represents indeterminate progress, in which case the
progress view ignores `total`.

## See Also

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(_:value:total:)

Creates a progress view for showing determinate progress that generates its
label from a localized string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        value: V?,
        total: V = 1.0
    ) where Label == Text, CurrentValueLabel == EmptyView, V : BinaryFloatingPoint

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`titleKey`

    

The key for the progress view’s localized title that describes the task in
progress.

`value`

    

The completed amount of the task to this point, in a range of `0.0` to
`total`, or `nil` if the progress is indeterminate.

`total`

    

The full amount representing the complete scope of the task, meaning the task
is complete if `value` equals `total`. The default value is `1.0`.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the
progress view pins the value to those limits, rounding to the nearest possible
bound. A value of `nil` represents indeterminate progress, in which case the
progress view ignores `total`.

This initializer creates a `Text` view on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings. To initialize a determinate
progress view with a string variable, use the corresponding initializer that
takes a `StringProtocol` instance.

## See Also

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(_:value:total:)

Creates a progress view for showing determinate progress that generates its
label from a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S, V>(
        _ title: S,
        value: V?,
        total: V = 1.0
    ) where Label == Text, CurrentValueLabel == EmptyView, S : StringProtocol, V : BinaryFloatingPoint

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`title`

    

The string that describes the task in progress.

`value`

    

The completed amount of the task to this point, in a range of `0.0` to
`total`, or `nil` if the progress is indeterminate.

`total`

    

The full amount representing the complete scope of the task, meaning the task
is complete if `value` equals `total`. The default value is `1.0`.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the
progress view pins the value to those limits, rounding to the nearest possible
bound. A value of `nil` represents indeterminate progress, in which case the
progress view ignores `total`.

This initializer creates a `Text` view on your behalf, and treats the title
similar to `init(verbatim:)`. See `Text` for more information about localizing
strings. To initialize a determinate progress view with a localized string
key, use the corresponding initializer that takes a `LocalizedStringKey`
instance.

## See Also

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(value:total:label:)

Creates a progress view for showing determinate progress, with a custom label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<V>(
        value: V?,
        total: V = 1.0,
        @ViewBuilder label: () -> Label
    ) where CurrentValueLabel == EmptyView, V : BinaryFloatingPoint

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`value`

    

The completed amount of the task to this point, in a range of `0.0` to
`total`, or `nil` if the progress is indeterminate.

`total`

    

The full amount representing the complete scope of the task, meaning the task
is complete if `value` equals `total`. The default value is `1.0`.

`label`

    

A view builder that creates a view that describes the task in progress.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the
progress view pins the value to those limits, rounding to the nearest possible
bound. A value of `nil` represents indeterminate progress, in which case the
progress view ignores `total`.

## See Also

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label, currentValueLabel: () ->
CurrentValueLabel)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(value:total:label:currentValueLabel:)

Creates a progress view for showing determinate progress, with a custom label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<V>(
        value: V?,
        total: V = 1.0,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel
    ) where V : BinaryFloatingPoint

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`value`

    

The completed amount of the task to this point, in a range of `0.0` to
`total`, or `nil` if the progress is indeterminate.

`total`

    

The full amount representing the complete scope of the task, meaning the task
is complete if `value` equals `total`. The default value is `1.0`.

`label`

    

A view builder that creates a view that describes the task in progress.

`currentValueLabel`

    

A view builder that creates a view that describes the level of completed
progress of the task.

## Discussion

If the value is non-`nil`, but outside the range of `0.0` through `total`, the
progress view pins the value to those limits, rounding to the nearest possible
bound. A value of `nil` represents indeterminate progress, in which case the
progress view ignores `total`.

## See Also

### Creating a determinate progress view

`init(Progress)`

Creates a progress view for visualizing the given progress instance.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V)`

Creates a progress view for showing determinate progress.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(LocalizedStringKey, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a localized string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<S, V>(S, value: V?, total: V)`

Creates a progress view for showing determinate progress that generates its
label from a string.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

`init<V>(value: V?, total: V, label: () -> Label)`

Creates a progress view for showing determinate progress, with a custom label.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(timerInterval:countsDown:)

Creates a progress view for showing continuous progress as time passes.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        timerInterval: ClosedRange<Date>,
        countsDown: Bool = true
    )

Available when `Label` is `EmptyView` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

##  Parameters

`timerInterval`

    

The date range over which the view progresses.

`countsDown`

    

If `true` (the default), the view empties as time passes.

## Discussion

Use this initializer to create a view that shows continuous progress within a
date range. The following example initializes a progress view with a range of
`start...end`, where `start` is 30 seconds in the past and `end` is 90 seconds
in the future. As a result, the progress view begins at 25 percent complete.

By default, the progress view empties as time passes from the start of the
date range to the end, but you can use the `countsDown` parameter to create a
progress view that fills as time passes, as the above example demonstrates.

The progress view provided by this initializer omits a descriptive label and
provides a text label that automatically updates to describe the current time
remaining. To provide custom views for these labels, use
`init(value:total:label:currentValueLabel:)` instead.

Note

Date-relative progress views, such as those created with this initializer,
don’t support custom styles.

## See Also

### Create a progress view spanning a date range

`init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label)`

Creates a progress view for showing continuous progress as time passes, with a
descriptive label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

`init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label,
currentValueLabel: () -> CurrentValueLabel)`

Creates a progress view for showing continuous progress as time passes, with
descriptive and current progress labels.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(timerInterval:countsDown:label:)

Creates a progress view for showing continuous progress as time passes, with a
descriptive label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        timerInterval: ClosedRange<Date>,
        countsDown: Bool = true,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

##  Parameters

`timerInterval`

    

The date range over which the view progresses.

`countsDown`

    

A Boolean value that determines whether the view empties or fills as time
passes. If `true` (the default), the view empties.

`label`

    

An optional view that describes the purpose of the progress view.

## Discussion

Use this initializer to create a view that shows continuous progress within a
date range. The following example initializes a progress view with a range of
`start...end`, where `start` is 30 seconds in the past and `end` is 90 seconds
in the future. As a result, the progress view begins at 25 percent complete.
This example also provides a custom descriptive label.

By default, the progress view empties as time passes from the start of the
date range to the end, but you can use the `countsDown` parameter to create a
progress view that fills as time passes, as the above example demonstrates.

The progress view provided by this initializer uses a text label that
automatically updates to describe the current time remaining. To provide a
custom label to show the current value, use
`init(value:total:label:currentValueLabel:)` instead.

Note

Date-relative progress views, such as those created with this initializer,
don’t support custom styles.

## See Also

### Create a progress view spanning a date range

`init(timerInterval: ClosedRange<Date>, countsDown: Bool)`

Creates a progress view for showing continuous progress as time passes.

Available when `Label` is `EmptyView` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

`init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label,
currentValueLabel: () -> CurrentValueLabel)`

Creates a progress view for showing continuous progress as time passes, with
descriptive and current progress labels.

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

Initializer

# init(timerInterval:countsDown:label:currentValueLabel:)

Creates a progress view for showing continuous progress as time passes, with
descriptive and current progress labels.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        timerInterval: ClosedRange<Date>,
        countsDown: Bool = true,
        @ViewBuilder label: () -> Label,
        @ViewBuilder currentValueLabel: () -> CurrentValueLabel
    )

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

##  Parameters

`timerInterval`

    

The date range over which the view should progress.

`countsDown`

    

A Boolean value that determines whether the view empties or fills as time
passes. If `true` (the default), the view empties.

`label`

    

An optional view that describes the purpose of the progress view.

`currentValueLabel`

    

A view that displays the current value of the timer.

## Discussion

Use this initializer to create a view that shows continuous progress within a
date range. The following example initializes a progress view with a range of
`start...end`, where `start` is 30 seconds in the past and `end` is 90 seconds
in the future. As a result, the progress view begins at 25 percent complete.
This example also provides custom views for a descriptive label (Progress) and
a current value label that shows the date range.

By default, the progress view empties as time passes from the start of the
date range to the end, but you can use the `countsDown` parameter to create a
progress view that fills as time passes, as the above example demonstrates.

Note

Date-relative progress views, such as those created with this initializer,
don’t support custom styles.

## See Also

### Create a progress view spanning a date range

`init(timerInterval: ClosedRange<Date>, countsDown: Bool)`

Creates a progress view for showing continuous progress as time passes.

Available when `Label` is `EmptyView` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

`init(timerInterval: ClosedRange<Date>, countsDown: Bool, label: () -> Label)`

Creates a progress view for showing continuous progress as time passes, with a
descriptive label.

Available when `Label` conforms to `View` and `CurrentValueLabel` is
`DefaultDateProgressLabel`.

Initializer

# init(_:)

Creates a progress view based on a style configuration.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ configuration: ProgressViewStyleConfiguration) where Label == ProgressViewStyleConfiguration.Label, CurrentValueLabel == ProgressViewStyleConfiguration.CurrentValueLabel

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to
`View`.

## Discussion

You can use this initializer within the `makeBody(configuration:)` method of a
`ProgressViewStyle` to create an instance of the styled progress view. This is
useful for custom progress view styles that only modify the current progress
view style, as opposed to implementing a brand new style. Because this
modifier style can’t know how the current style represents progress, avoid
making assumptions about the view’s contents, such as whether it uses bars or
other shapes.

The following example shows a style that adds a rounded pink border to a
progress view, but otherwise preserves the progress view’s current style:

Note

Progress views in widgets don’t apply custom styles.

