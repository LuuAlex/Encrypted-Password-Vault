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

func runPythonCode(read: Bool) -> PythonObject {
    let sys = Python.import("sys")
    sys.path.append("/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault")
    let file = Python.import("script.py")
    if read {
        return file.read()
    } else {
        return file.write()
    }
}
