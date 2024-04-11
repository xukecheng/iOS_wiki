Initializer

# init(_:)

Create an `AccessibilityCustomContentKey` with the specified label.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(_ labelKey: LocalizedStringKey)

##  Parameters

`labelKey`

    

Localized text describing to the user what is contained in this additional
information entry. For example: “orientation”. This will also be used as the
identifier.

## See Also

### Creating a key

`init(Text, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

`init(LocalizedStringKey, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

Initializer

# init(_:id:)

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ label: Text,
        id: String
    )

##  Parameters

`label`

    

Localized text describing to the user what is contained in this additional
information entry. For example: “orientation”.

`id`

    

String used to identify the additional information entry to SwiftUI. Adding an
entry will replace any previous value with the same identifier.

## See Also

### Creating a key

`init(LocalizedStringKey)`

Create an `AccessibilityCustomContentKey` with the specified label.

`init(LocalizedStringKey, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

Initializer

# init(_:id:)

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ labelKey: LocalizedStringKey,
        id: String
    )

##  Parameters

`labelKey`

    

Localized text describing to the user what is contained in this additional
information entry. For example: “orientation”.

`id`

    

String used to identify the additional information entry to SwiftUI. Adding an
entry will replace any previous value with the same identifier.

## See Also

### Creating a key

`init(LocalizedStringKey)`

Create an `AccessibilityCustomContentKey` with the specified label.

`init(Text, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

