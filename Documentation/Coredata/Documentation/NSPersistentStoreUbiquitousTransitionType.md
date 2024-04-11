Enumeration Case

# NSPersistentStoreUbiquitousTransitionType.accountAdded

This value indicates that a new iCloud account is available, and the
persistent store in use will or did transition to the new account.

iOS 7.0–10.0  Deprecated  iPadOS 7.0–10.0  Deprecated  macOS 10.9–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    case accountAdded = 1

## Discussion

It is only possible to discern this state when the application is running, and
therefore this transition type will only be posted if the account changes
while the application is running or in the background.

Enumeration Case

# NSPersistentStoreUbiquitousTransitionType.accountRemoved

This value indicates that no iCloud account is available, and the persistent
store in use will or did transition to the “local” store.

iOS 7.0–10.0  Deprecated  iPadOS 7.0–10.0  Deprecated  macOS 10.9–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    case accountRemoved = 2

## Discussion

It is only possible to discern this state when the application is running, and
therefore this transition type will only be posted if the account is removed
while the application is running or in the background.

Enumeration Case

# NSPersistentStoreUbiquitousTransitionType.contentRemoved

This value indicates that the user has wiped the contents of the iCloud
account, usually using Delete All from Documents & Data in Settings.

iOS 7.0–10.0  Deprecated  iPadOS 7.0–10.0  Deprecated  macOS 10.9–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    case contentRemoved = 3

## Discussion

The Core Data integration will transition to an empty store file as a result
of this event.

Enumeration Case

# NSPersistentStoreUbiquitousTransitionType.initialImportCompleted

This value indicates that the Core Data integration has finished building a
store file that is consistent with the contents of the iCloud account, and is
ready to replace the fallback store with that file.

iOS 7.0–10.0  Deprecated  iPadOS 7.0–10.0  Deprecated  macOS 10.9–10.12
Deprecated  Mac Catalyst 13.1–13.1  Deprecated  visionOS 1.0–1.0  Deprecated

    
    
    case initialImportCompleted = 4

