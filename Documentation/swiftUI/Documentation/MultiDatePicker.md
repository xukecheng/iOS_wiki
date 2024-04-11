Initializer

# init(_:selection:)

Creates an instance that selects multiple dates with an unbounded range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Set<DateComponents>>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

## See Also

### Picking dates

`init<S>(S, selection: Binding<Set<DateComponents>>)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, label: () -> Label)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` conforms to `View`.

Initializer

# init(_:selection:)

Creates an instance that selects multiple dates with an unbounded range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Set<DateComponents>>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

## See Also

### Picking dates

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, label: () -> Label)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` conforms to `View`.

Initializer

# init(selection:label:)

Creates an instance that selects multiple dates with an unbounded range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<Set<DateComponents>>,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date values being displayed and selected.

`label`

    

A view that describes the use of the dates.

## See Also

### Picking dates

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>)`

Creates an instance that selects multiple dates with an unbounded range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates in a range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Set<DateComponents>>,
        in bounds: Range<Date>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The exclusive range of selectable dates.

## See Also

### Picking dates in a range

`init<S>(S, selection: Binding<Set<DateComponents>>, in: Range<Date>)`

Creates an instance that selects multiple dates in a range.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: Range<Date>, label: () ->
Label)`

Creates an instance that selects multiple dates in a range.

Available when `Label` conforms to `View`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates in a range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Set<DateComponents>>,
        in bounds: Range<Date>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The exclusive range of selectable dates.

## See Also

### Picking dates in a range

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
Range<Date>)`

Creates an instance that selects multiple dates in a range.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: Range<Date>, label: () ->
Label)`

Creates an instance that selects multiple dates in a range.

Available when `Label` conforms to `View`.

Initializer

# init(selection:in:label:)

Creates an instance that selects multiple dates in a range.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<Set<DateComponents>>,
        in bounds: Range<Date>,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date values being displayed and selected.

`bounds`

    

The exclusive range of selectable dates.

`label`

    

A view that describes the use of the dates.

## See Also

### Picking dates in a range

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
Range<Date>)`

Creates an instance that selects multiple dates in a range.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>, in: Range<Date>)`

Creates an instance that selects multiple dates in a range.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates on or after some start date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeFrom<Date>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range from some selectable start date.

## See Also

### Picking dates after a date

`init<S>(S, selection: Binding<Set<DateComponents>>, in:
PartialRangeFrom<Date>)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: PartialRangeFrom<Date>,
label: () -> Label)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` conforms to `View`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates on or after some start date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeFrom<Date>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range from some selectable start date.

## See Also

### Picking dates after a date

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
PartialRangeFrom<Date>)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: PartialRangeFrom<Date>,
label: () -> Label)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` conforms to `View`.

Initializer

# init(selection:in:label:)

Creates an instance that selects multiple dates on or after some start date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeFrom<Date>,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range from some selectable start date.

`label`

    

A view that describes the use of the dates.

## See Also

### Picking dates after a date

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
PartialRangeFrom<Date>)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>, in:
PartialRangeFrom<Date>)`

Creates an instance that selects multiple dates on or after some start date.

Available when `Label` is `Text`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates before some end date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeUpTo<Date>
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range before some end date.

## See Also

### Picking dates before a date

`init<S>(S, selection: Binding<Set<DateComponents>>, in:
PartialRangeUpTo<Date>)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: PartialRangeUpTo<Date>,
label: () -> Label)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` conforms to `View`.

Initializer

# init(_:selection:in:)

Creates an instance that selects multiple dates before some end date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeUpTo<Date>
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title of `self`, describing its purpose.

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range before some end date.

## See Also

### Picking dates before a date

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
PartialRangeUpTo<Date>)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` is `Text`.

`init(selection: Binding<Set<DateComponents>>, in: PartialRangeUpTo<Date>,
label: () -> Label)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` conforms to `View`.

Initializer

# init(selection:in:label:)

Creates an instance that selects multiple dates before some end date.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<Set<DateComponents>>,
        in bounds: PartialRangeUpTo<Date>,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View`.

##  Parameters

`selection`

    

The date values being displayed and selected.

`bounds`

    

The open range before some end date.

`label`

    

A view that describes the use of the dates.

## See Also

### Picking dates before a date

`init(LocalizedStringKey, selection: Binding<Set<DateComponents>>, in:
PartialRangeUpTo<Date>)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Set<DateComponents>>, in:
PartialRangeUpTo<Date>)`

Creates an instance that selects multiple dates before some end date.

Available when `Label` is `Text`.

