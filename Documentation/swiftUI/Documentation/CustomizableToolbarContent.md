Instance Method

# defaultCustomization()

Configures customizable toolbar content with the default visibility and
options.

iOS 16.0–16.0  Deprecated  iPadOS 16.0–16.0  Deprecated  macOS 13.0–13.0
Deprecated  Mac Catalyst 16.0–16.0  Deprecated  tvOS 16.0–16.0  Deprecated
watchOS 9.0–9.0  Deprecated  visionOS 1.0+

    
    
    func defaultCustomization() -> some CustomizableToolbarContent
    

## Discussion

Use the `defaultCustomization(_:options:)` modifier providing either a
`defaultVisibility` or `options` instead.

## See Also

### Using default options

`func defaultCustomization(Visibility, options: ToolbarCustomizationOptions)
-> some CustomizableToolbarContent`

Configures the way customizable toolbar items with the default behavior
behave.

Instance Method

# defaultCustomization(_:options:)

Configures the way customizable toolbar items with the default behavior
behave.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func defaultCustomization(
        _ defaultVisibility: Visibility = .automatic,
        options: ToolbarCustomizationOptions = []
    ) -> some CustomizableToolbarContent
    

##  Parameters

`defaultVisibility`

    

The default visibility of toolbar content with the default customization
behavior.

`options`

    

The customization options to configure the behavior of toolbar content with
the default customization behavior.

## Discussion

Default customizable items support a variety of edits by the user.

  * A user can add an an item that is not in the toolbar.

  * A user can remove an item that is in the toolbar.

  * A user can move an item within the toolbar.

By default, all default customizable items will be initially present in the
toolbar. Provide a value of `Visibility.hidden` to this modifier to specify
that items should initially be hidden from the user, and require them to add
those items to the toolbar if desired.

You can ensure that the user can always use an item with default
customizability, even if it’s removed from the customizable toolbar. To do
this, provide the `alwaysAvailable` option. Unlike a customizable item with a
customization behavior of `ToolbarCustomizationBehavior/none` which always
remain in the toolbar itself, these items will remain in the overflow if the
user removes them from the toolbar.

Provide a value of `alwaysAvailable` to the options parameter of this modifier
to receive this behavior.

## See Also

### Using default options

`func defaultCustomization() -> some CustomizableToolbarContent`

Configures customizable toolbar content with the default visibility and
options.

Instance Method

# customizationBehavior(_:)

Configures the customization behavior of customizable toolbar content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func customizationBehavior(_ behavior: ToolbarCustomizationBehavior) -> some CustomizableToolbarContent
    

##  Parameters

`behavior`

    

The customization behavior of the customizable toolbar content.

## Discussion

Customizable toolbar items support different kinds of customization:

  * A user can add an an item that is not in the toolbar.

  * A user can remove an item that is in the toolbar.

  * A user can move an item within the toolbar.

Based on the customization behavior of the toolbar items, different edits will
be supported.

Use this modifier to the customization behavior a user can perform on your
toolbar items. In the following example, the customizable toolbar item
supports all of the different kinds of toolbar customizations and starts in
the toolbar.

You can create an item that can not be removed from the toolbar or moved
within the toolbar by passing a value of `disabled` to this modifier.

You can create an item that can not be removed from the toolbar, but can be
moved by passing a value of `reorderable`.

