Initializer

# init(selection:supportsOpacity:label:)

Creates an instance that selects a color.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<Color>,
        supportsOpacity: Bool = true,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`selection`

    

A `Binding` to the variable that displays the selected `Color`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjusting the
selected color’s opacity; the default is `true`.

`label`

    

A view that describes the use of the selected color. The system color picker
UI sets it’s title using the text from this view.

## See Also

### Creating a color picker

`init(LocalizedStringKey, selection: Binding<Color>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string key.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<Color>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:selection:supportsOpacity:)

Creates a color picker with a text label generated from a title string key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<Color>,
        supportsOpacity: Bool = true
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the picker.

`selection`

    

A `Binding` to the variable that displays the selected `Color`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjustments to
the selected color’s opacity; the default is `true`.

## Discussion

Use `ColorPicker` to create a color well that your app uses to allow the
selection of a `Color`. The example below creates a color well using a
`Binding` to a property stored in a settings object and title you provide:

## See Also

### Creating a color picker

`init(selection: Binding<Color>, supportsOpacity: Bool, label: () -> Label)`

Creates an instance that selects a color.

`init<S>(S, selection: Binding<Color>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:selection:supportsOpacity:)

Creates a color picker with a text label generated from a title string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<Color>,
        supportsOpacity: Bool = true
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title displayed by the color picker.

`selection`

    

A `Binding` to the variable containing a `Color`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjustments to
the selected color’s opacity; the default is `true`.

## Discussion

Use `ColorPicker` to create a color well that your app uses to allow the
selection of a `Color`. The example below creates a color well using a
`Binding` and title you provide:

## See Also

### Creating a color picker

`init(selection: Binding<Color>, supportsOpacity: Bool, label: () -> Label)`

Creates an instance that selects a color.

`init(LocalizedStringKey, selection: Binding<Color>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string key.

Available when `Label` is `Text`.

Initializer

# init(selection:supportsOpacity:label:)

Creates an instance that selects a color.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        selection: Binding<CGColor>,
        supportsOpacity: Bool = true,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`selection`

    

A `Binding` to the variable that displays the selected `CGColor`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjusting the
selected color’s opacity; the default is `true`.

`label`

    

A view that describes the use of the selected color. The system color picker
UI sets it’s title using the text from this view.

## See Also

### Creating a core graphics color picker

`init(LocalizedStringKey, selection: Binding<CGColor>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string key.

Available when `Label` is `Text`.

`init<S>(S, selection: Binding<CGColor>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:selection:supportsOpacity:)

Creates a color picker with a text label generated from a title string key.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        selection: Binding<CGColor>,
        supportsOpacity: Bool = true
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title of the picker.

`selection`

    

A `Binding` to the variable that displays the selected `CGColor`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjustments to
the selected color’s opacity; the default is `true`.

## See Also

### Creating a core graphics color picker

`init(selection: Binding<CGColor>, supportsOpacity: Bool, label: () -> Label)`

Creates an instance that selects a color.

`init<S>(S, selection: Binding<CGColor>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string.

Available when `Label` is `Text`.

Initializer

# init(_:selection:supportsOpacity:)

Creates a color picker with a text label generated from a title string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        selection: Binding<CGColor>,
        supportsOpacity: Bool = true
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

The title displayed by the color picker.

`selection`

    

A `Binding` to the variable containing a `CGColor`.

`supportsOpacity`

    

A Boolean value that indicates whether the color picker allows adjustments to
the selected color’s opacity; the default is `true`.

## See Also

### Creating a core graphics color picker

`init(selection: Binding<CGColor>, supportsOpacity: Bool, label: () -> Label)`

Creates an instance that selects a color.

`init(LocalizedStringKey, selection: Binding<CGColor>, supportsOpacity: Bool)`

Creates a color picker with a text label generated from a title string key.

Available when `Label` is `Text`.

