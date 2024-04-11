Type Property

# automatic

The default style for date pickers.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    static var automatic: DefaultDatePickerStyle { get }

Available when `Self` is `DefaultDatePickerStyle`.

## See Also

### Getting built-in date picker styles

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

Type Property

# compact

A date picker style that displays the components in a compact, textual format.

iOS 14.0+  iPadOS 14.0+  macOS 10.15.4+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    static var compact: CompactDatePickerStyle { get }

Available when `Self` is `CompactDatePickerStyle`.

## Discussion

Use this style when space is constrained and users expect to make specific
date and time selections. Some variants may include rich editing controls in a
pop up.

## See Also

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

Type Property

# field

A date picker style that displays the components in an editable field.

macOS 10.15+

    
    
    static var field: FieldDatePickerStyle { get }

Available when `Self` is `FieldDatePickerStyle`.

## Discussion

You can use this style when space is constrained and users expect to make
specific date and time selections. However, you should generally use
`stepperField` instead of this style, unless your your app requires hiding the
stepper.

## See Also

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

Type Property

# graphical

A date picker style that displays an interactive calendar or clock.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var graphical: GraphicalDatePickerStyle { get }

Available when `Self` is `GraphicalDatePickerStyle`.

## Discussion

This style is useful when you want to allow browsing through days in a
calendar, or when the look of a clock face is appropriate.

## See Also

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

Type Property

# stepperField

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

macOS 10.15+

    
    
    static var stepperField: StepperFieldDatePickerStyle { get }

Available when `Self` is `StepperFieldDatePickerStyle`.

## Discussion

This style is useful when space is constrained and users expect to make
specific date and time selections.

## See Also

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var wheel: WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Available when `Self` is `WheelDatePickerStyle`.

Type Property

# wheel

A date picker style that displays each component as columns in a scrollable
wheel.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 10.0+  visionOS 1.0+

    
    
    static var wheel: WheelDatePickerStyle { get }

Available when `Self` is `WheelDatePickerStyle`.

## See Also

### Getting built-in date picker styles

`static var automatic: DefaultDatePickerStyle`

The default style for date pickers.

Available when `Self` is `DefaultDatePickerStyle`.

`static var compact: CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

Available when `Self` is `CompactDatePickerStyle`.

`static var field: FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

Available when `Self` is `FieldDatePickerStyle`.

`static var graphical: GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

Available when `Self` is `GraphicalDatePickerStyle`.

`static var stepperField: StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

Available when `Self` is `StepperFieldDatePickerStyle`.

Instance Method

# makeBody(configuration:)

Returns the appearance and interaction content for a `DatePicker`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration `

    

The properties of the date picker.

## Discussion

The system calls this method for each `DatePicker` instance in a view
hierarchy where this style is the current date picker style.

## See Also

### Creating custom date picker styles

`struct DatePickerStyleConfiguration`

The properties of a `DatePicker`.

`typealias Configuration`

A type alias for the properties of a `DatePicker`.

`associatedtype Body : View`

A view representing the appearance and interaction of a `DatePicker`.

**Required**

Structure

# DatePickerStyleConfiguration

The properties of a `DatePicker`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    struct DatePickerStyleConfiguration

## Topics

### Establishing the date range

`var minimumDate: Date?`

The oldest selectable date.

`var maximumDate: Date?`

The most recent selectable date.

### Labeling the date picker

`let label: DatePickerStyleConfiguration.Label`

A description of the `DatePicker`.

`struct Label`

A type-erased label of a `DatePicker`.

`var displayedComponents: DatePickerComponents`

The date components that the user is able to view and edit.

### Selecting the date

`var selection: Date`

The date value being displayed and selected.

`var $selection: Binding<Date>`

## See Also

### Creating custom date picker styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Returns the appearance and interaction content for a `DatePicker`.

**Required**

` typealias Configuration`

A type alias for the properties of a `DatePicker`.

`associatedtype Body : View`

A view representing the appearance and interaction of a `DatePicker`.

**Required**

Type Alias

# DatePickerStyle.Configuration

A type alias for the properties of a `DatePicker`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    typealias Configuration = DatePickerStyleConfiguration

## See Also

### Creating custom date picker styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Returns the appearance and interaction content for a `DatePicker`.

**Required**

` struct DatePickerStyleConfiguration`

The properties of a `DatePicker`.

`associatedtype Body : View`

A view representing the appearance and interaction of a `DatePicker`.

**Required**

Associated Type

# Body

A view representing the appearance and interaction of a `DatePicker`.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom date picker styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Returns the appearance and interaction content for a `DatePicker`.

**Required**

` struct DatePickerStyleConfiguration`

The properties of a `DatePicker`.

`typealias Configuration`

A type alias for the properties of a `DatePicker`.

Structure

# DefaultDatePickerStyle

The default style for date pickers.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 10.0+
visionOS 1.0+

    
    
    struct DefaultDatePickerStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the default date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Structure

# CompactDatePickerStyle

A date picker style that displays the components in a compact, textual format.

iOS 14.0+  iPadOS 14.0+  macOS 10.15.4+  Mac Catalyst 13.4+  visionOS 1.0+

    
    
    struct CompactDatePickerStyle

## Overview

You can also use `compact` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the compact date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Structure

# FieldDatePickerStyle

A date picker style that displays the components in an editable field.

macOS 10.15+

    
    
    struct FieldDatePickerStyle

## Overview

You can also use `field` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the field date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Structure

# GraphicalDatePickerStyle

A date picker style that displays an interactive calendar or clock.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct GraphicalDatePickerStyle

## Overview

You can also use `graphical` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the graphical date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Structure

# StepperFieldDatePickerStyle

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

macOS 10.15+

    
    
    struct StepperFieldDatePickerStyle

## Overview

You can also use `stepperField` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the field date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct WheelDatePickerStyle`

A date picker style that displays each component as columns in a scrollable
wheel.

Structure

# WheelDatePickerStyle

A date picker style that displays each component as columns in a scrollable
wheel.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 10.0+  visionOS 1.0+

    
    
    struct WheelDatePickerStyle

## Overview

You can also use `wheel` to construct this style.

## Topics

### Creating the date picker style

`init()`

Creates an instance of the wheel date picker style.

## Relationships

### Conforms To

  * `DatePickerStyle`

## See Also

### Suporting types

`struct DefaultDatePickerStyle`

The default style for date pickers.

`struct CompactDatePickerStyle`

A date picker style that displays the components in a compact, textual format.

`struct FieldDatePickerStyle`

A date picker style that displays the components in an editable field.

`struct GraphicalDatePickerStyle`

A date picker style that displays an interactive calendar or clock.

`struct StepperFieldDatePickerStyle`

A system style that displays the components in an editable field, with
adjoining stepper that can increment/decrement the selected component.

