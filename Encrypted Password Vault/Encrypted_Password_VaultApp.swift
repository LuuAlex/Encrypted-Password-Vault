//
//  Encrypted_Password_VaultApp.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/12/23.
//

import SwiftUI
import PythonKit

@main
struct Encrypted_Password_VaultApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}


func runCreateCSV(path: String, password: String) {
    PythonLibrary.useLibrary(at: "/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault/.venv/bin/python3")
    let os = Python.import("os")
    let base64 = Python.import("base64")
    let csv = Python.import("csv")
    let cryptography = Python.import("cryptography")
    let Fernet = Python.import("cryptography.fernet")
    let hashes = Python.import("cryptography.hazmat.primitives")
    let PBKDF2HMAC = Python.import("ryptography.hazmat.primitives.kdf.pbkdf2")

    
    let sys = Python.import("sys")
    sys.path.append("/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault")
    let file = Python.import("script.py")
    file.create_csv(path, password)
}

func runRead(path: String, password: String) -> [DataObject] {
    PythonLibrary.useLibrary(at: "/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault/.venv/bin/python3")
    let os = Python.import("os")
    let base64 = Python.import("base64")
    let csv = Python.import("csv")
    let cryptography = Python.import("cryptography")
    let Fernet = Python.import("cryptography.fernet")
    let hashes = Python.import("cryptography.hazmat.primitives")
    let PBKDF2HMAC = Python.import("ryptography.hazmat.primitives.kdf.pbkdf2")
    
    
    let sys = Python.import("sys")
    sys.path.append("/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault")
    let file = Python.import("script.py")
    var data = String(file.read(path, password))!
    var dataArray: [DataObject] = []
    
    var dataItems: [String] = data.components(separatedBy: "\\r\\s")
    for item: String in dataItems {
        dataArray.append(DataObject(array: item.components(separatedBy: ",")))
    }
    return dataArray
}
