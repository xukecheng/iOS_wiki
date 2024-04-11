Enumeration Case

# NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType

Specifies that the context will be associated with a private dispatch queue.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case privateQueueConcurrencyType = 1

## See Also

### Concurrency Types

`case mainQueueConcurrencyType`

Specifies that the context will be associated with the main queue.

`case confinementConcurrencyType`

Specifies that the context will use the thread confinement pattern.

Deprecated

Enumeration Case

# NSManagedObjectContextConcurrencyType.mainQueueConcurrencyType

Specifies that the context will be associated with the main queue.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    case mainQueueConcurrencyType = 2

## See Also

### Concurrency Types

`case privateQueueConcurrencyType`

Specifies that the context will be associated with a private dispatch queue.

`case confinementConcurrencyType`

Specifies that the context will use the thread confinement pattern.

Deprecated

Enumeration Case

# NSManagedObjectContextConcurrencyType.confinementConcurrencyType

Specifies that the context will use the thread confinement pattern.

iOS 3.0–9.0  Deprecated  iPadOS 3.0–9.0  Deprecated  macOS 10.4–10.11
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  tvOS 9.0–9.0  Deprecated
watchOS 2.0–2.0  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    case confinementConcurrencyType = 0

## See Also

### Concurrency Types

`case privateQueueConcurrencyType`

Specifies that the context will be associated with a private dispatch queue.

`case mainQueueConcurrencyType`

Specifies that the context will be associated with the main queue.

