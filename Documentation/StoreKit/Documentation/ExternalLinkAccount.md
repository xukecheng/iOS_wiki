Type Property

# canOpen

A Boolean value that indicates whether the app can open the external link
account.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 17.4+  tvOS 16.4+  Xcode 14.0+

    
    
    static var canOpen: Bool { get async }

## Discussion

Check this property before showing any user-interface controls that enable
people to open the external link account.

Don’t check this property again in response to user input; instead, call
`open()` immediately.

Important

Only show user-interface controls that call the `open()` method if this
property is `true`. The `open()` method always throws an error when `canOpen`
is `false`.

## See Also

### Linking to external accounts

`static func open()`

Presents a continuation sheet that enables people to choose whether to open
your app’s link to an external website for account creation or management.

Type Method

# open()

Presents a continuation sheet that enables people to choose whether to open
your app’s link to an external website for account creation or management.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 17.4+  tvOS 16.4+  Xcode 14.0+

    
    
    static func open() async throws

## Discussion

Call this method in response to deliberate user interaction, for example,
tapping a button. Call `canOpen` to determine whether to display a button or
other user-interface control. If `canOpen` is `false`, this method always
throws a `StoreKitError` instance.

## See Also

### Linking to external accounts

`static var canOpen: Bool`

A Boolean value that indicates whether the app can open the external link
account.
