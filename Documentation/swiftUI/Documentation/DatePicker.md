Initializer

# init(selection:displayedComponents:label:)

Creates an instance that selects a `Date` with an unbounded range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        selection: Binding<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date],
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date value being displayed and selected.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

`label`

    

A view that describes the use of the date.

## See Also

### Creating a date picker for any date

`init(LocalizedStringKey, selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components)`

Creates an instance that selects a `Date` with an unbounded range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components)`

Creates an instance that selects a `Date` within the given range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:displayedComponents:)

Creates an instance that selects a `Date` with an unbounded range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker for any date

`init(selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` with an unbounded range.

Available when `Label` conforms to `View`.

`init<S>(S, selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components)`

Creates an instance that selects a `Date` within the given range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:displayedComponents:)

Creates an instance that selects a `Date` within the given range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker for any date

`init(selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` with an unbounded range.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, displayedComponents:
DatePicker<Label>.Components)`

Creates an instance that selects a `Date` with an unbounded range.

Available when `Label` is `Text`.

Initializer

# init(selection:in:displayedComponents:label:)

Creates an instance that selects a `Date` in a closed range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        selection: Binding<Date>,
        in range: ClosedRange<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date],
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date value being displayed and selected.

`range`

    

The inclusive range of selectable dates.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

`label`

    

A view that describes the use of the date.

## See Also

### Creating a date picker for a range

`init(LocalizedStringKey, selection: Binding<Date>, in: ClosedRange<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, in: ClosedRange<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` in a closed range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Date>,
        in range: ClosedRange<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The inclusive range of selectable dates.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker for a range

`init(selection: Binding<Date>, in: ClosedRange<Date>, displayedComponents:
DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` conforms to `View`.

`init<S>(S, selection: Binding<Date>, in: ClosedRange<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` in a closed range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Date>,
        in range: ClosedRange<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The inclusive range of selectable dates.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker for a range

`init(selection: Binding<Date>, in: ClosedRange<Date>, displayedComponents:
DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, in: ClosedRange<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` in a closed range.

Available when `Label` is `Text`.

Initializer

# init(selection:in:displayedComponents:label:)

Creates an instance that selects a `Date` on or after some start date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        selection: Binding<Date>,
        in range: PartialRangeFrom<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date],
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date value being displayed and selected.

`range`

    

The open range from some selectable start date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

`label`

    

A view that describes the use of the date.

## See Also

### Creating a date picker with a start date

`init(LocalizedStringKey, selection: Binding<Date>, in:
PartialRangeFrom<Date>, displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, in: PartialRangeFrom<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` on or after some start date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Date>,
        in range: PartialRangeFrom<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The open range from some selectable start date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker with a start date

`init(selection: Binding<Date>, in: PartialRangeFrom<Date>,
displayedComponents: DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` conforms to `View`.

`init<S>(S, selection: Binding<Date>, in: PartialRangeFrom<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` on or after some start date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Date>,
        in range: PartialRangeFrom<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The open range from some selectable start date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker with a start date

`init(selection: Binding<Date>, in: PartialRangeFrom<Date>,
displayedComponents: DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, in:
PartialRangeFrom<Date>, displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or after some start date.

Available when `Label` is `Text`.

Initializer

# init(selection:in:displayedComponents:label:)

Creates an instance that selects a `Date` on or before some end date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        selection: Binding<Date>,
        in range: PartialRangeThrough<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date],
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date value being displayed and selected.

`range`

    

The open range before some selectable end date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

`label`

    

A view that describes the use of the date.

## See Also

### Creating a date picker with an end date

`init(LocalizedStringKey, selection: Binding<Date>, in:
PartialRangeThrough<Date>, displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Date>, in: PartialRangeThrough<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` on or before some end date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Date>,
        in range: PartialRangeThrough<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The open range before some selectable end date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker with an end date

`init(selection: Binding<Date>, in: PartialRangeThrough<Date>,
displayedComponents: DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` conforms to `View`.

`init<S>(S, selection: Binding<Date>, in: PartialRangeThrough<Date>,
displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:displayedComponents:)

Creates an instance that selects a `Date` on or before some end date.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Date>,
        in range: PartialRangeThrough<Date>,
        displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date value being displayed and selected.

`range`

    

The open range before some selectable end date.

`displayedComponents`

    

The date components that user is able to view and edit. Defaults to
`[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or
`.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker with an end date

`init(selection: Binding<Date>, in: PartialRangeThrough<Date>,
displayedComponents: DatePicker<Label>.Components, label: () -> Label)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` conforms to `View`.

`init(LocalizedStringKey, selection: Binding<Date>, in:
PartialRangeThrough<Date>, displayedComponents: DatePicker<Label>.Components)`

Creates an instance that selects a `Date` on or before some end date.

Available when `Label` is `Text`.

Type Alias

# DatePicker.Components

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    typealias Components = DatePickerComponents

## See Also

### Setting date picker components

`struct DatePickerComponents`

Structure

# DatePickerComponents

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    struct DatePickerComponents

## Topics

### Getting date picker components

`static let date: DatePickerComponents`

Displays day, month, and year based on the locale

`static let hourAndMinute: DatePickerComponents`

Displays hour and minute components based on the locale

`static let hourMinuteAndSecond: DatePickerComponents`

Displays hour, minute and second components based on the locale

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Setting date picker components

`typealias Components`

