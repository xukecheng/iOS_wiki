Type Property

# automatic

The default picker style, based on the picker’s context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var automatic: DefaultPickerStyle { get }

Available when `Self` is `DefaultPickerStyle`.

## Discussion

How a picker using the default picker style appears largely depends on the
platform and the view type in which it appears. For example, in a standard
view, the default picker styles by platform are:

  * On iOS and watchOS the default is a wheel.

  * On macOS, the default is a pop-up button.

  * On tvOS, the default is a segmented control.

The default picker style may also take into account other factors — like
whether the picker appears in a container view — when setting the appearance
of a picker.

You can override a picker’s style. To apply the default style to a picker, or
to a view that contains pickers, use the `pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# inline

A `PickerStyle` where each option is displayed inline with other views in the
current container.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var inline: InlinePickerStyle { get }

Available when `Self` is `InlinePickerStyle`.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# menu

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static var menu: MenuPickerStyle { get }

Available when `Self` is `MenuPickerStyle`.

## Discussion

Use this style when there are more than five options. Consider using `inline`
when there are fewer than five options.

The button itself indicates the selected option. You can include additional
controls in the set of options, such as a button to customize the list of
options.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# navigationLink

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    static var navigationLink: NavigationLinkPickerStyle { get }

Available when `Self` is `NavigationLinkPickerStyle`.

## Discussion

In navigation stacks, prefer the default `menu` style. Consider the navigation
link style when you have a large number of options or your design is better
expressed by pushing onto a stack.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# palette

A picker style that presents the options as a row of compact elements.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static var palette: PalettePickerStyle { get }

Available when `Self` is `PalettePickerStyle`.

## Discussion

Note

When used outside of menus, this style is rendered as a segmented picker. If
that is the intended usage, consider `segmented` instead.

For each option’s label, use one symbol per item, if you add more than 6
options, the picker scrolls horizontally on iOS.

The following example creates a palette picker:

Palette pickers will display the selection of untinted SF Symbols or template
images by applying the system tint. For tinted SF Symbols, a stroke is
outlined around the symbol upon selection. If you would like to supply a
particular image (or SF Symbol) to signify selection, we suggest using
`custom`. This deactivates any system selection behavior, allowing the
provided image to solely indicate selection instead.

The following example creates a palette picker that disables the system
selection behaviour:

If a specific SF Symbol variant is preferable instead, use
`symbolVariant(_:)`:

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# radioGroup

A picker style that presents the options as a group of radio buttons.

macOS 10.15+

    
    
    static var radioGroup: RadioGroupPickerStyle { get }

Available when `Self` is `RadioGroupPickerStyle`.

## Discussion

Use this style when there are two to five options. Consider using `menu` when
there are more than five options.

For each option’s label, use sentence-style capitalization without ending
punctuation, like a period or colon.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# segmented

A picker style that presents the options in a segmented control.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    static var segmented: SegmentedPickerStyle { get }

Available when `Self` is `SegmentedPickerStyle`.

## Discussion

Use this style when there are two to five options. Consider using `menu` when
there are more than five options.

For each option’s label, use sentence-style capitalization without ending
punctuation, like a period or colon.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var wheel: WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Available when `Self` is `WheelPickerStyle`.

Type Property

# wheel

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 6.0+  visionOS 1.0+

    
    
    static var wheel: WheelPickerStyle { get }

Available when `Self` is `WheelPickerStyle`.

## Discussion

Because most options aren’t visible, organize them in a predictable order,
such as alphabetically.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

## See Also

### Getting built-in picker styles

`static var automatic: DefaultPickerStyle`

The default picker style, based on the picker’s context.

Available when `Self` is `DefaultPickerStyle`.

`static var inline: InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

Available when `Self` is `InlinePickerStyle`.

`static var menu: MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

Available when `Self` is `MenuPickerStyle`.

`static var navigationLink: NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

Available when `Self` is `NavigationLinkPickerStyle`.

`static var palette: PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

Available when `Self` is `PalettePickerStyle`.

`static var radioGroup: RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

Available when `Self` is `RadioGroupPickerStyle`.

`static var segmented: SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Available when `Self` is `SegmentedPickerStyle`.

Structure

# DefaultPickerStyle

The default picker style, based on the picker’s context.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct DefaultPickerStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a default picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# InlinePickerStyle

A `PickerStyle` where each option is displayed inline with other views in the
current container.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct InlinePickerStyle

## Overview

You can also use `inline` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates an inline picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# MenuPickerStyle

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct MenuPickerStyle

## Overview

You can also use `menu` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a menu picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# NavigationLinkPickerStyle

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    struct NavigationLinkPickerStyle

## Overview

In navigation stacks, prefer the default `menu` style. Consider the navigation
link style when you have a large number of options or your design is better
expressed by pushing onto a stack.

You can also use `navigationLink` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a navigation link picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# PalettePickerStyle

A picker style that presents the options as a row of compact elements.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct PalettePickerStyle

## Overview

You can also use `palette` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a palette picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# RadioGroupPickerStyle

A picker style that presents the options as a group of radio buttons.

macOS 10.15+

    
    
    struct RadioGroupPickerStyle

## Overview

You can also use `radioGroup` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a radio group picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# SegmentedPickerStyle

A picker style that presents the options in a segmented control.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    struct SegmentedPickerStyle

## Overview

You can also use `segmented` to construct this style.

## Topics

### Creating the picker style

`init()`

Creates a segmented picker style.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct WheelPickerStyle`

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

Structure

# WheelPickerStyle

A picker style that presents the options in a scrollable wheel that shows the
selected option and a few neighboring options.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  watchOS 6.0+  visionOS 1.0+

    
    
    struct WheelPickerStyle

## Overview

You can also use `wheel` to construct this style.

## Topics

### Creating the picker style

`init()`

Sets the picker style to display an item wheel from which the user makes a
selection.

## Relationships

### Conforms To

  * `PickerStyle`

## See Also

### Supporting types

`struct DefaultPickerStyle`

The default picker style, based on the picker’s context.

`struct InlinePickerStyle`

A `PickerStyle` where each option is displayed inline with other views in the
current container.

`struct MenuPickerStyle`

A picker style that presents the options as a menu when the user presses a
button, or as a submenu when nested within a larger menu.

`struct NavigationLinkPickerStyle`

A picker style represented by a navigation link that presents the options by
pushing a List-style picker view.

`struct PalettePickerStyle`

A picker style that presents the options as a row of compact elements.

`struct RadioGroupPickerStyle`

A picker style that presents the options as a group of radio buttons.

`struct SegmentedPickerStyle`

A picker style that presents the options in a segmented control.

Structure

# PopUpButtonPickerStyle

A picker style that presents the options as a menu when the user presses a
button.

macOS 10.15–14.4  Deprecated

    
    
    struct PopUpButtonPickerStyle

Deprecated

Use `MenuPickerStyle` instead.

## Overview

Use this style when there are more than five options. Consider using
`RadioGroupPickerStyle` when there are fewer than five options.

The button itself indicates the selected option. You can include additional
controls in the set of options, such as a button to customize the list of
options.

To apply this style to a picker, or to a view that contains pickers, use the
`pickerStyle(_:)` modifier.

### Creating the picker style

  * `init()`

## Topics

### Initializers

`init()`

Creates a pop-up button picker style.

## Relationships

### Conforms To

  * `PickerStyle`

