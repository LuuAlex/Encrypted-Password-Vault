//
//  UserDataJSON.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/17/23.
//

import Foundation


struct UserData: Codable {
    var path: String
    var hashedPassword: String
}

func initalize() {
    encodeJSON(userData: UserData(path: "", hashedPassword: ""))
}


func checkPathExists() -> Bool {
    if getPath() != nil {
        return true
    }
    return false
}

func checkPasswordExists() -> Bool {
    if getPassword() != nil {
        return true
    }
    return false
}


func checkHashedPassword(password: String) -> Bool {
    let userData = getPassword()
    if userData != nil {
        return userData == password
    }
    return false
}

func getPath() -> String? {
    let userData = decodeJSON()
    if userData != nil {
        return userData?.path
    }
    return nil
}

func getPassword() -> String? {
    let userData = decodeJSON()
    if userData != nil {
        return userData?.hashedPassword
    }
    return nil
}

func setPath(path: String) {
    encodeJSON(userData: UserData(path: path, hashedPassword: getPassword() ?? ""))
}

func setPassword(password: String) {
    encodeJSON(userData: UserData(path: getPath() ?? "", hashedPassword: password))
}


func decodeJSON() -> UserData? {
    do {
        let fileURL = URL(fileURLWithPath: FileManager.default.currentDirectoryPath).appendingPathComponent("userData.json")
        let data = try Data(contentsOf: fileURL, options: .alwaysMapped)
        
        let decoder = JSONDecoder()
        let dataDecoded = try decoder.decode(UserData.self, from: data)
        return dataDecoded
    } catch {
        print("Unable to parse JSON file")
    }
    return nil
}

func encodeJSON(userData: UserData) {
    let encoder = JSONEncoder()
    do {
        let fileURL = URL(fileURLWithPath: FileManager.default.currentDirectoryPath).appendingPathComponent("userData.json")
        let data = try encoder.encode(userData)
        try data.write(to: fileURL, options: .atomic)
    } catch {
        print("Error in encoding JSON")
    }
}
