Type Property

# automatic

Use the a dismissal behavior that’s appropriate for the given context.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static let automatic: MenuActionDismissBehavior

## Discussion

In most cases, the default behavior is `enabled`. There are some cases, like
`Stepper`, that use `disabled` by default.

## See Also

### Getting dismiss behaviors

`static let disabled: MenuActionDismissBehavior`

Never dismiss the presented menu after performing an action.

`static let enabled: MenuActionDismissBehavior`

Always dismiss the presented menu after performing an action.

Type Property

# disabled

Never dismiss the presented menu after performing an action.

iOS 16.4+  iPadOS 16.4+  Mac Catalyst 16.4+  tvOS 17.0+  visionOS 1.0+

    
    
    static let disabled: MenuActionDismissBehavior

## See Also

### Getting dismiss behaviors

`static let automatic: MenuActionDismissBehavior`

Use the a dismissal behavior that’s appropriate for the given context.

`static let enabled: MenuActionDismissBehavior`

Always dismiss the presented menu after performing an action.

Type Property

# enabled

Always dismiss the presented menu after performing an action.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    static let enabled: MenuActionDismissBehavior

## See Also

### Getting dismiss behaviors

`static let automatic: MenuActionDismissBehavior`

Use the a dismissal behavior that’s appropriate for the given context.

`static let disabled: MenuActionDismissBehavior`

Never dismiss the presented menu after performing an action.

