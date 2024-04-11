Instance Property

# minimumDate

The oldest selectable date.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    var minimumDate: Date?

## See Also

### Establishing the date range

`var maximumDate: Date?`

The most recent selectable date.

Instance Property

# maximumDate

The most recent selectable date.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    var maximumDate: Date?

## See Also

### Establishing the date range

`var minimumDate: Date?`

The oldest selectable date.

Instance Property

# label

A description of the `DatePicker`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    let label: DatePickerStyleConfiguration.Label

## See Also

### Labeling the date picker

`struct Label`

A type-erased label of a `DatePicker`.

`var displayedComponents: DatePickerComponents`

The date components that the user is able to view and edit.

Structure

# DatePickerStyleConfiguration.Label

A type-erased label of a `DatePicker`.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Labeling the date picker

`let label: DatePickerStyleConfiguration.Label`

A description of the `DatePicker`.

`var displayedComponents: DatePickerComponents`

The date components that the user is able to view and edit.

Instance Property

# displayedComponents

The date components that the user is able to view and edit.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    var displayedComponents: DatePickerComponents

## See Also

### Labeling the date picker

`let label: DatePickerStyleConfiguration.Label`

A description of the `DatePicker`.

`struct Label`

A type-erased label of a `DatePicker`.

Instance Property

# selection

The date value being displayed and selected.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    @Binding
    var selection: Date { get nonmutating set }

## See Also

### Selecting the date

`var $selection: Binding<Date>`

Instance Property

# $selection

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 10.0+
visionOS 1.0+

    
    
    var $selection: Binding<Date> { get }

## See Also

### Selecting the date

`var selection: Date`

The date value being displayed and selected.

