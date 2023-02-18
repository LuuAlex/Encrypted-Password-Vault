//
//  UserDataJSON.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/17/23.
//

import Foundation

struct UserData: Codable {
    var hashedPassword: String
    var path: String
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

func writeJSON(userData: UserData) {
    let encoder = JSONEncoder()
    do {
        let fileURL = URL(fileURLWithPath: FileManager.default.currentDirectoryPath).appendingPathComponent("userData.json")
        let data = try encoder.encode(userData)
        try data.write(to: fileURL, options: .atomic)
    } catch {
        print("Error in encoding JSON")
    }
}

func getPath() -> String? {
    let userData = decodeJSON()
    if userData != nil {
        return userData?.path
    }
    return nil
}

func checkHashedPassword(password: String) -> Bool {
    let userData = decodeJSON()
    if userData != nil {
        return userData?.hashedPassword == password
    }
    return false
}
