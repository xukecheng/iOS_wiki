Initializer

# init(_:destination:)

Creates a control, consisting of a URL and a title key, used to navigate to a
URL.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        destination: URL
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title that describes the purpose of this link.

`destination`

    

The URL for the link.

## Discussion

Use `Link` to create a control that your app uses to navigate to a URL that
you provide. The example below creates a link to `example.com` and uses `Visit
Example Co` as the title key to generate a link-styled view in your app:

## See Also

### Creating a link

`init<S>(S, destination: URL)`

Creates a control, consisting of a URL and a title string, used to navigate to
a URL.

Available when `Label` is `Text`.

`init(destination: URL, label: () -> Label)`

Creates a control, consisting of a URL and a label, used to navigate to the
given URL.

Initializer

# init(_:destination:)

Creates a control, consisting of a URL and a title string, used to navigate to
a URL.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        destination: URL
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

A text string used as the title for describing the underlying `destination`
URL.

`destination`

    

The URL for the link.

## Discussion

Use `Link` to create a control that your app uses to navigate to a URL that
you provide. The example below creates a link to `example.com` and displays
the title string you provide as a link-styled view in your app:

## See Also

### Creating a link

`init(LocalizedStringKey, destination: URL)`

Creates a control, consisting of a URL and a title key, used to navigate to a
URL.

Available when `Label` is `Text`.

`init(destination: URL, label: () -> Label)`

Creates a control, consisting of a URL and a label, used to navigate to the
given URL.

Initializer

# init(destination:label:)

Creates a control, consisting of a URL and a label, used to navigate to the
given URL.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        destination: URL,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`destination`

    

The URL for the link.

`label`

    

A view that describes the destination of URL.

## See Also

### Creating a link

`init(LocalizedStringKey, destination: URL)`

Creates a control, consisting of a URL and a title key, used to navigate to a
URL.

Available when `Label` is `Text`.

`init<S>(S, destination: URL)`

Creates a control, consisting of a URL and a title string, used to navigate to
a URL.

Available when `Label` is `Text`.

