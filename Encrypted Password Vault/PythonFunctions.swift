//
//  PythonFunctions.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/17/23.
//

import Foundation
import PythonKit
import Python

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
    sys.path.append("/Users/alexluu/Developer/Personal/Encrypted Password Vault/Encrypted Password Vault")
    let file = Python.import("script")
    file.create_csv(path, password)
}

func runRead(path: String, password: String) -> [DataObject] {
    activate()

    let sys = Python.import("sys")
    sys.path.append("/Users/alexluu/Developer/Personal/Encrypted Password Vault/Encrypted Password Vault")
    let file = Python.import("script")
    print("\(file.read(path, password))")
    let data = String(file.read(path, password)) ?? "xxx" // TODO: file is not reading correctly
    print(path)
    print(password)
    print(data)
    var dataArray: [DataObject] = []
    
    let dataItems: [String] = data.components(separatedBy: "\\r\\n")
    for item: String in dataItems {
        dataArray.append(DataObject(array: item.components(separatedBy: ",")))
    }
    return dataArray
}

func runWrite(path: String, password: String, newDataEntry: [String]) {
    activate()

    let sys = Python.import("sys")
    sys.path.append("/Users/alexluu/Developer/Personal/Encrypted Password Vault/Encrypted Password Vault")
    let file = Python.import("script")
    file.write(path, password, newDataEntry)
}
