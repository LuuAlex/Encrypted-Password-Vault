//
//  Encrypted_Password_VaultApp.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/12/23.
//

import SwiftUI
import PythonKit
import Foundation
import Python

@main
struct Encrypted_Password_VaultApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}



func activate() {
    guard let stdLibPath = Bundle.main.path(forResource: "python-stdlib", ofType: nil) else { return }
    guard let libDynloadPath = Bundle.main.path(forResource: "python-stdlib/lib-dynload", ofType: nil) else { return }
    setenv("PYTHONHOME", stdLibPath, 1)
    setenv("PYTHONPATH", "\(stdLibPath):\(libDynloadPath)", 1)
    Py_Initialize()
}

func runCreateCSV(path: String, password: String) {
    activate()
    
    let sys = Python.import("sys")
    sys.path.append("/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault")
    let file = Python.import("script.py")
    file.create_csv(path, password)
}

func runRead(path: String, password: String) -> [DataObject] {
    activate()

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
